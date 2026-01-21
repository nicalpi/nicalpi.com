#!/usr/bin/env python3
"""
Export HTML to JPEG/PNG for The Calm CTO brand assets.

Usage:
    python3 export_image.py input.html output.jpg
    python3 export_image.py input.html output.png --width 1080 --height 1080
    python3 export_image.py input.html output.jpg --quality 90 --scale 2

Requirements:
    pip install playwright --break-system-packages
    playwright install chromium
"""

import argparse
import asyncio
import sys
from pathlib import Path


async def export_image(
    input_path: str,
    output_path: str,
    width: int = 1200,
    height: int = 630,
    quality: int = 95,
    scale: float = 2.0,
):
    """Render HTML file to image using Playwright."""

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("Error: playwright not installed.")
        print("Run: pip install playwright --break-system-packages")
        print("Then: playwright install chromium")
        sys.exit(1)

    input_file = Path(input_path).resolve()
    output_file = Path(output_path).resolve()

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    # Determine output format
    output_format = output_file.suffix.lower()
    if output_format not in ['.jpg', '.jpeg', '.png']:
        print(f"Error: Unsupported output format: {output_format}")
        print("Supported formats: .jpg, .jpeg, .png")
        sys.exit(1)

    is_jpeg = output_format in ['.jpg', '.jpeg']

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        page = await browser.new_page(
            viewport={'width': width, 'height': height},
            device_scale_factor=scale,
        )

        # Load the HTML file
        await page.goto(f'file://{input_file}')

        # Wait for fonts to load
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(0.5)  # Extra time for font rendering

        # Take screenshot at high resolution
        screenshot_options = {
            'type': 'jpeg' if is_jpeg else 'png',
            'clip': {
                'x': 0,
                'y': 0,
                'width': width,
                'height': height,
            },
        }

        if is_jpeg:
            screenshot_options['quality'] = quality

        screenshot_bytes = await page.screenshot(**screenshot_options)

        # If scale > 1, resize back to target dimensions for correct OG image size
        if scale > 1:
            try:
                from PIL import Image
                import io

                img = Image.open(io.BytesIO(screenshot_bytes))
                img = img.resize((width, height), Image.Resampling.LANCZOS)

                if is_jpeg:
                    img.save(str(output_file), 'JPEG', quality=quality)
                else:
                    img.save(str(output_file), 'PNG')
            except ImportError:
                # Fallback: save at scaled size if PIL not available
                print("Warning: PIL not installed. Output will be scaled up.")
                print("Run: pip install Pillow --break-system-packages")
                with open(output_file, 'wb') as f:
                    f.write(screenshot_bytes)
        else:
            with open(output_file, 'wb') as f:
                f.write(screenshot_bytes)

        await browser.close()

    # Calculate file size
    size_kb = output_file.stat().st_size / 1024

    print(f"Exported: {output_file.name}")
    print(f"   Size: {width} x {height}px ({size_kb:.1f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description='Export HTML to JPEG/PNG image',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 export_image.py header.html header.jpg
  python3 export_image.py quote.html quote.png --width 1080 --height 1080
  python3 export_image.py stats.html stats.jpg --quality 85 --scale 1
        """
    )

    parser.add_argument('input', help='Input HTML file')
    parser.add_argument('output', help='Output image file (.jpg, .jpeg, or .png)')
    parser.add_argument('--width', type=int, default=1200, help='Canvas width (default: 1200)')
    parser.add_argument('--height', type=int, default=630, help='Canvas height (default: 630)')
    parser.add_argument('--quality', type=int, default=95, help='JPEG quality 1-100 (default: 95)')
    parser.add_argument('--scale', type=float, default=2.0, help='Device scale for retina (default: 2.0)')

    args = parser.parse_args()

    asyncio.run(export_image(
        args.input,
        args.output,
        width=args.width,
        height=args.height,
        quality=args.quality,
        scale=args.scale,
    ))


if __name__ == '__main__':
    main()
