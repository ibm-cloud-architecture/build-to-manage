# Build To Manage

We all have been there before: Development throws their new code over the wall, and Operations has to figure out how to deploy, how to monitor, how to manage it. In the traditional world, development had time to build this knowledge. Applications were updated rarely, and once deployed the lifetime of the application could span years. As the velocity and speed of change increases, operations teams can become a bottleneck, resulting in either a decelerated release or an increase of operational risks.

Continued Deploy is a key theme in the cloud world, which means that Operations have significant less time to build the knowledge, and the opportunity to apply this knowledge is much shorter. Therefore, we need a different approach to management. Instead of Operations figuring out their tasks in isolation, Development provides information on how to manage the application. In DevOps, developers already took control of one important aspect of operations: Deployment and Release of the application. However, there are more things developers should do to ease operations.

As organizations are working on building out a sustainable culture, we recognize the need for some simple specific steps to follow to start getting some of the benefits in the short term. To this end, we are introducing a new approach to operations which we call Build to Manage. It specifies the practice of activities developers can do in order to instrument the application, or provide manageability aspects as part of an application release. 

![Build To Manage](https://github.com/ibm-cloud-architecture/build-to-manage/blob/master/BTM.png "Build To Manage")


The “Build to Manage” approach includes the following aspects:

-	HealthCheck API
-	Log Format and Catalog	
-	Deployment correlation
-	Distributed Tracing
-	Topology Information
-	Event Format and Catalog
-	Test Cases and Scripts
-	Runbooks
-	First Failure Data Capture


Sample code and links to demonstrate the principles outlined in the Build to Manage Point of View document

### HealthAPI
- Python
  - [Basic Python examples](HealthCheckAPIs/python/)
  - [Runscope Python HealthCheck example](https://github.com/Runscope/healthcheck)
- Node.js
  - [Broadly NodeJS HealthCheck example](https://github.com/broadly/node-healthchecks)
- Ruby
  - [SportsEngine Ruby on Rails HealthCheck example](https://github.com/sportngin/okcomputer)

### Log management
- Java
  - [eGym Java Log management example](https://github.com/egymgmbh/log-queue)

### Distributed tracing and logging
- Node.js
   - [Diagnostics Working Group](https://github.com/nodejs/diagnostics)
- Python
  - [Basic Python examples](DistributedTrace/python/)
- Java (framework)
  - [Spring Cloud Sleuth](https://cloud.spring.io/spring-cloud-sleuth/)

#### Open Tracing
[**OpenTracing**](https://github.com/opentracing/specification/blob/master/specification.md) is a distributed tracing instrumentation standard. It aims to standarize instrumentation, so developers can instrument first, and worry about the collection/distribution/aggregation system later. OpenTracing’s foundational concepts are Traces and Spans. Traces are the “story” of a transaction or workflow as it makes its way through a system. They are represented as directed acyclic graphs. A trace is made up of spans, which each represent one component of the story. Each trace starts with a span. Spans create new spans with two types of relationships that express both the semantics in the system (FollowFrom), and the critical path for latency-sensitive (distributed) operations (ChildOf).

Current languages with [OpenTracing API libraries](http://opentracing.io/documentation/pages/api/api-implementations.html)
- [Go](https://github.com/opentracing/opentracing-go)
- [Python](https://github.com/opentracing/opentracing-python) doesn’t support tracers yet, so unusable in production
- [Javascript](https://github.com/opentracing/opentracing-javascript) not sufficient by itself, and required library to make it work is not yet finished
- [Objective-C](https://github.com/opentracing/opentracing-objc)
- [Java](https://github.com/opentracing/opentracing-java) requires explicit tracer instantiation
- [C++](https://github.com/opentracing/opentracing-cpp) needs some work - this library uses C++98


### First Failure Data Capture
- Node.js
  - [nodereport Delivers a human-readable diagnostic summary](https://github.com/nodejs/nodereport)
  - [llnode Plugin for LLDB a next generation, high-performance debugger](https://github.com/nodejs/llnode)



