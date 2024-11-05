---
layout: post
title: "Reassessing Ruby on Rails Conventions: A Fresh Look at Testing, Authentication, Front-End Management, Background Jobs, Caching, and Deployment"
subtitle: "Feeling like a failure can be overwhelming, but it doesn’t have to define you. After a year of setbacks and struggles, I decided to take a different approach—one rooted in consistency over perfection. In this post, I share how I’m committing to daily actions for the next 3 months to create lasting change and regain purpose by showing up every day, no matter what."
description: "Feeling like a failure can be overwhelming, but it doesn’t have to define you. After a year of setbacks and struggles, I decided to take a different approach—one rooted in consistency over perfection. In this post, I share how I’m committing to daily actions for the next 3 months to create lasting change and regain purpose by showing up every day, no matter what."
image: "assets/images/posts/feeling-like-a-failure.jpg"
tags: rails
---
I’ve been working with Ruby on Rails since 2008, and over the years, I’ve witnessed the framework evolve in remarkable ways.
With Rails 8.0 on the horizon and a new side project on my plate, I figured it’s the perfect time to reevaluate the the tools I'll use.
In this post, I’ll share my thought process as I navigate the choices for testing, authentication, front-end management, background jobs, caching, and deployment in a new Rails project.

## “Convention Over Configuration”—But with a Twist

Ruby on Rails thrives on the philosophy of “convention over configuration,” streamlining development by providing sensible defaults.
This approach accelerates setup and lets developers focus on building features rather than fiddling with configurations.

But, let's face it, when you have been using the tools for a long time, it's easy to fall into a routine and stick with what you know.

However, starting a new project—especially with the upcoming Rails 8.0—seems like an ideal moment to revisit my default tools to ensure they’re still the best fit for my needs.

Development Styles vs. Feature Development

In Rails, conventions can be broadly classified into two categories:

	•	Development Style Conventions: These dictate project structure, framework behavior, and naming expectations. They’ve largely remained unchanged, providing a consistent foundation that makes it easier for teams to collaborate and maintain codebases.
	•	Feature/gem conventions: These influence how you implement tests, authentication, background jobs, and more. This area is more fluid, with various tools and libraries offering different approaches.

While development style conventions offer a solid and familiar structure, the multitude of options for feature development can be both a blessing and a curse.

So, let's pause before running `rails new digestive` and take a moment to evaluate my options. Working solo this time, free from team considerations and time constraints, it’s the perfect opportunity to explore and learn.

## 1. Testing: Minitest vs. RSpec

Testing is non-negotiable for me, even on side projects. It serves as a safety net when building new code but also accelerates my development by using tests as a building roadmap for what I want to acheive.
Writing tests ensures features work as intended without constantly switching to the browser for manual checks.

In the Rails ecosystem, the two main camps for testing are Minitest and RSpec.

### Minitest

[Minitest](https://github.com/minitest/minitest) is the default testing framework bundled with Rails. It’s lightweight, fast, and requires no additional setup. Its style is akin to the default Ruby testing framework, Test::Unit, which is great if you’re already familiar with it. While it might be less expressive than RSpec, it’s notably faster.

Here’s an example using Minitest:

```ruby
# test/models/user_test.rb
require 'test_helper'

class UserTest < ActiveSupport::TestCase
  test "should not save user without email" do
    user = User.new(name: "Alice")
    assert_not user.save, "Saved the user without an email"
  end
end
```

What I appreciate about Minitest is its simplicity and speed. The built-in integration means no extra gems are needed, and parallel testing is supported by default. The straightforward syntax makes it easy to write and understand tests.

However, Minitest lacks some of the expressive DSL features found in other frameworks. Its ecosystem is smaller, so there are fewer plugins and extensions compared to RSpec.

### RSpec

[Rspec](https://github.com/minitest/minitest) is renowned for its readable and expressive syntax, aligning with the behavior-driven development (BDD) style of writing tests. This can be a significant advantage depending on your team’s preferences.

Personally, I’ve been using RSpec for the past 10 years, and I find it more expressive and easier to read. However, I admit I’m biased. One caveat with RSpec is that without proper structure, tests can become slow, which can be a hassle to manage.

Here’s how a test looks in RSpec:

```ruby
# spec/models/user_spec.rb
require 'rails_helper'

RSpec.describe User, type: :model do
  it "does not save without an email" do
    user = User.new(name: "Alice")
    expect(user.save).to be_falsey
  end
end
```

RSpec’s expressive syntax reads almost like plain English, improving readability. It boasts an extensive community with numerous plugins and extensions. Its BDD focus encourages thinking about user behavior and outcomes, which can lead to more robust tests.

The downside is that RSpec requires additional setup—you need to add the gem and configure the test environment. There’s also a slight performance overhead due to its richer feature set.

### My Choice

If I were starting a new project with my team, I’d likely stick with RSpec since we’re all familiar with it. However, since I’m flying solo on this project, I’m opting for Minitest. I’m intrigued by its simpler setup, faster test runs, and overall performance. Plus, it’s an excellent opportunity for me to learn something new.
{: .callout-yellow}

## 2. Authentication

Most web and mobile apps need some form of authentication—typically creating a user with a password and email. While Rails now offers built-in ways to handle authentication with has_secure_password, there are other options worth considering.

### Rails Built-in Authentication

This new addition in Rails 8.0 provides a new 'straightforward way' to handle basic user authentication. Running `bin/rails generate authentication` generates a User model with password handling and a couple of desirable like sign-in form and reset password flow. However registration is not generated yet, you will have to get this done manully.

You can check an overview in the video made by [Superails](https://www.youtube.com/watch?v=bD2oL1lUnKA)

Here’s a snippet from the generated User model:

```ruby
class User < ApplicationRecord
  has_secure_password
  has_many :sessions, dependent: :destroy

  normalizes :email_address, with: ->(e) { e.strip.downcase }
end
```

I appreciate this integrated solution because it doesn’t require external dependencies, and you have full control over the authentication process and code. It’s great for basic authentication needs.

However, it has limited features. I'm also wondering how to maintain it as it
evolves. Say a new security vulnerability is discovered, I would probably have
to handle the patch myself?

### Authentication Zero

[Authentication Zero](https://github.com/lazaronixon/authentication-zero) is a lightweight generator that sets up a complete authentication system without unnecessary complexity. I guess it's what rails authentication strived to be in the near future.

You can install it with:

```bash
bundle add authentication_zero
rails g authentication_zero:install
```

The advantage here is that it generates customizable code, including essentials like password resets, email confirmations, invitations, etc without adding much overhead.

On the flip side, it has a smaller community, so there’s less documentation and support compared to more popular solutions. You’re also responsible for maintaining the generated code.

### Devise

[Devise](https://github.com/heartcombo/devise) is a well-established authentication solution with a comprehensive feature set. It’s been around for quite some time and comes with everything you might need, but at the cost of complexity. Customizing it to your specific needs can be challenging, and since the gem acts as a black box (unlike Rails’ built-in auth or Authentication Zero, which generate code you can modify), it might not be ideal for everyone.

You can set up Devise with:

```ruby
bundle add devise

rails generate devise:install
rails generate devise User
```

Devise handles authentication, registration, password recovery, and more. It has extensive documentation and a vibrant community with numerous extensions.

The downsides are its complexity and the learning curve involved in understanding all its configurations and options.

### My Choice

Rails doesn't lack choices in the authentication department, those 3 options are
solid, and I could also have mentionned Sorcery, Clearance, Authlogic or even
Rodauth.

But, for this project, after a ton of mental back and forth, to give the new Rails Authentication a go. I know my project auth will be simple, and, worst scenario, I can always switch to another solution later on.
{: .callout-yellow}

## 3. Front-End Management: Navigating the Options

Modern web applications require efficient management of JavaScript and CSS assets. This is one area where Rails keeps evolving, offering multiple options that align with current trends.

I event wrote a long recap of my thoughts on X a few months ago. You can read it
[here on X/@nicalpi](https://x.com/nicalpi/status/1711690017918030011).

### Importmap

[Importmap-Rails](https://github.com/rails/importmap-rails) allows you to manage JavaScript modules without a bundler, leveraging the browser’s native ES module support. You can set it up with:

```bash
rails new app_name --javascript=importmap
```

And use it like this:

```javascript
// app/javascript/application.js
import "@hotwired/turbo-rails"
import "controllers"
```

The beauty of Importmap is that it doesn’t require Node.js, simplifying the development and deployment environment. It’s quick to set up and ideal for smaller projects or those who prefer minimal tooling.

However, it has limited library support—not all libraries are available as ES modules. I also find it somewhat awkward to use since there’s no straightforward way to include npm packages. You often have to rely on CDN versions of libraries or download them into your repository.

### ESBuild

ESBuild with [jsbundling-rails](https://github.com/rails/jsbundling-rails) is an ultra-fast JavaScript bundler and minifier. You can set it up with:

```bash
rails new app_name --javascript=esbuild
```

ESBuild offers blazing-fast build times and handles the latest JavaScript features. It optimizes the final bundle size through tree shaking and minification.

The catch is that it requires Node.js, adding a dependency to your project. Its ecosystem is less mature compared to something like Webpack, so there are fewer plugins available. It also requires some configuration for custom setups.

### Other Options

The Rails ecosystem offers even more choices like Webpacker (now Shakapacker), Vite, and Parcel. Each has its own set of pros and cons, and the best choice often depends on the specific needs of your project.

### My Choice

For this project, I aim for simplicity without sacrificing performance. ESBuild strikes a good balance with its speed and modern features. I've also chosen to use Tailwind on the front with a component library called [https://preline.co](Preline.co). Unfortunately, Preline doesn't play nicely with importmaps, so, for now, I'm gonna stay with ESBuild and enjoy the simplicity.
{: .callout-yellow}

## 4. Background Jobs

Handling tasks asynchronously is essential for a responsive user experience—whether it’s sending emails, processing complex computations, or doing heavy lifting in the background. When it comes to background jobs in Rails, there are several options, but with Rails 8.0, there’s a new kid on the block.

### Solid Queue

[Solid Queue](https://github.com/rails/solid_queue) is a new background processing library that aims to provide a simple and efficient solution. It’s built into Rails, uses your existing database (no need to worry about managing Redis or other services), and is easy to set up.

The advantages are its simplicity and Active Record integration. However, being a new library, it might lack some advanced features, and community support is smaller compared to established solutions.

### Sidekiq

[Sidekiq](https://github.com/sidekiq/sidekiq) is the go-to option for many applications. It’s robust, well-maintained, and uses Redis for background job processing. It also offers paid options for more complex needs.

Here’s how you might use Sidekiq:

```ruby
# app/jobs/notification_job.rb
class NotificationJob
  include Sidekiq::Worker

  def perform(user_id)
    user = User.find(user_id)
    UserMailer.welcome_email(user).deliver_now
  end
end
```

Sidekiq excels in performance and can handle a large number of jobs efficiently. It supports concurrency and provides a web UI for monitoring jobs.

The downsides are the requirement of Redis, adding an external dependency, and a bit more complex setup.

### My Choice

I’ve been using Sidekiq for as long as I can remember and I’m happy with it. But Solid Queue is new and intriguing. For this project, I think I’ll give Solid Queue a try. It’s a good opportunity to learn something new, and I’m curious to see how it performs.
{: .callout-yellow}

## 5. Caching

Caching is another area where Rails offers multiple options out of the box, and with Rails 8.0, again, there’s a shiny new option: Solid Cache.

### Solid Cache

[Solid Cache](https://github.com/rails/solid_cache) aims to provide a simple and efficient caching solution for Rails applications. Like Solid Queue, it’s built into Rails and uses your existing database engine, eliminating the need for additional services.

I think it’s a solid option for my new project, especially since switching caching strategies in the future shouldn’t be too disruptive.

### Redis Cache Store

Alternatively, using Redis as a cache store offers persistence and scalability. Setting it up involves adding the Redis gem and configuring your environment:

```ruby
# In your Gemfile
gem 'redis'

# In config/environments/production.rb
config.cache_store = :redis_cache_store, { url: ENV['REDIS_URL'] }
```

Redis is scalable and data persists across server restarts. However, it requires managing a Redis server and additional configuration.

### My Choice

Given that I’m experimenting with Solid Queue for background jobs, it makes sense to try Solid Cache as well. It’s an area where trying something new shouldn’t have significant downsides, and I’m interested to see how it performs.
{: .callout-yellow}

## 6. Deployment

Deployment is a crucial piece of the puzzle. After all, coding is fun, but getting users is even better. Using Rails offers several options, and there’s a new one that’s caught my eye: Kamal.

### Kamal

[Kamal](https://github.com/basecamp/kamal) is a deployment tool designed for simplicity, using Docker containers. It seems to come with everything you might need to deploy a new application on a VPS or cloud provider.

The pros are streamlined deployments and consistent environments across development and production due to Docker. The cons are that it’s a newer tool with a smaller community, and it requires some understanding of Docker and Kamal’s workflow.

I’m currently halfway through a book on Kamal, and I highly recommend it if you want to learn more about deploying with this tool.

### Other Options: Heroku, Render, Fly.io, and Hatchbox.io

Heroku, Render, and Fly.io (and many more) are platform-as-a-service (PaaS) options that simplify deployments. Heroku, for instance, lets you deploy with a simple git push. These services handle scaling, load balancing, and offer easy integration with databases and other add-ons.

However, they can become expensive as your application scales, and you have less control over the environment. Performance can also be an issue, as you’re often sharing resources.

[Hatchbox.io](https://hatchbox.io) sits somewhere in the middle. It automates server provisioning and deployment on your own infrastructure, allowing you to deploy with a git push. It offers more control while still simplifying the deployment process, but it comes with a subscription fee and the responsibility of server maintenance.

### My Choice

I want to learn more about Kamal, especially to see if it’s something we should consider at work. So for this project, I’ll go with Kamal. If I were pressed for time, I’d probably opt for Hatchbox.io, as it offers a good balance between control and simplicity.
{: .callout-yellow}

## A few notable gems I can't live without

While I’m exploring new tools and conventions, there are a few gems that have become indispensable over the years. Here are a few I’ll be using in my new project:

  *	[Haml-Rails](https://github.com/haml/haml-rails): I'm sorry, I've tried
  again ERB, and I can't go back. I'm a lot more product in Haml, even more when
  considering the fact that I'll use Tailwind and its utility classes.
  * [Simple Form](https://github.com/heartcombo/simple_form): I think I'll
  inevitably end use using simple form. Rails form partial are absolutely fine,
  but I like the flexibility and simplicity of SimpleForm.
  * [Pundit](https://github.com/varvet/pundit): Another one that's technical not
  essential, but I like the way it forces me to think about authorization in a
  more structured way. I also like the way it's easy to test and write query
  scopes.
  * [Bullet](https://github.com/flyerhzm/bullet): A default in my Gemfile. I
  like to have it in development to catch N+1 queries and other performance
  issues.
  * [StandardRB](https://github.com/standardrb/standard): The only linter I can
  tolerate. I like the way it's opinionated and doesn't require much setup.
  * [View Components](https://github.com/ViewComponent/view_component): Not an
      essential for solo projects, but, when playgrouding the preline component
      library, it allowed to keep my views clean and organized.

## Wrapping Up

There are likely even more decisions to face when you’re about to run your rails new command. I recommend checking out all the options by typing rails new --help to see what’s available.

For me, the last decision was choosing a front-end framework. I’ve been using Bootstrap for as long as I can remember, so this side project is the perfect opportunity to try something new. I’m going to give Tailwind CSS a shot.

Here’s the command I’m using to set up my new project:

```bash
rails new digestive --database=postgresql -j esbuild --css tailwind
```

Embarking on this new project with Rails 8.0, I've also decided to build it in
public and share my progess here as well as on youtube, using it as a source for
small, bite-sized tutorials about the Rails ecosystem and features. If you want
to learn more, feel free to follow along on my journey.
