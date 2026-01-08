Chapter 6: Distributed Computing with Celery and Pyro4
Overview
This chapter demonstrates two powerful approaches to distributed computing in Python:

Celery - Distributed task queue for asynchronous job processing
Pyro4 - Python Remote Objects for distributed object communication
Both frameworks enable parallel processing across multiple machines and processes, making them essential tools for scalable application development.

Table of Contents
Prerequisites
Part 1: Celery Distributed Task Queue
Part 2: Pyro4 Remote Procedure Calls
Conclusions
Prerequisites
Required Packages
pip install celery
pip install Pyro4
Required Services
RabbitMQ (for Celery): Message broker for task distribution
Windows: Download from https://www.rabbitmq.com/download.html
Linux: sudo apt-get install rabbitmq-server
macOS: brew install rabbitmq
Part 1: Celery Distributed Task Queue
What is Celery?
Celery is an asynchronous task queue/job queue based on distributed message passing. It enables applications to distribute work across multiple worker processes or machines, making it ideal for:

Background task processing
Scheduled job execution
Distributed computation
Load balancing across workers
Files
addTask.py - Defines the Celery application and task
runAddTask.py - Executes the task asynchronously
Setup Instructions
Step 1: Start RabbitMQ Server
rabbitmq-server
Step 2: Start Celery Worker
Open a terminal and navigate to the chap6 directory:

celery -A addTask worker --loglevel=info --pool=solo
Note: On Windows, use --pool=solo to avoid multiprocessing issues.

Step 3: Run the Task
Open another terminal and run:

python runAddTask.py
Expected Output
Terminal 1 (Celery Worker):

-------------- celery@hostname v5.x.x
--- *** -----
-- *** ----
- * --- * ---
- ** ---------- [config]
- ** ---------- .> app:         addTask:0x...
- * ---------- .> transport:   amqp://guest:*@localhost:5672//
- ** ---------- .> results:     disabled://
- * --- * --- .> concurrency: 1 (solo)
-- *** ----
--- *** -----

[tasks]
  . addTask.add

[2026-01-01 00:00:00,000: INFO/MainProcess] Connected to amqp://guest:**@localhost:5672//
[2026-01-01 00:00:00,000: INFO/MainProcess] celery@hostname ready.
[2026-01-01 00:00:05,000: INFO/MainProcess] Task addTask.add[task-id] received
[2026-01-01 00:00:05,000: INFO/MainProcess] Task addTask.add[task-id] succeeded in 0.001s: 10
Terminal 2 (Task Execution):

Task ID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
Task Status: SUCCESS
Task Result: 10
How It Works
addTask.py creates a Celery application and defines an add task
The Celery worker connects to RabbitMQ and waits for tasks
runAddTask.py sends the task to the queue using delay() method
The worker picks up the task, executes it, and returns the result
The client retrieves the result using get() method
Part 2: Pyro4 Remote Procedure Calls
What is Pyro4?
Pyro4 (Python Remote Objects) enables transparent communication between Python objects across different processes or machines. It allows you to call methods on remote objects as if they were local, making distributed computing intuitive and Pythonic.

Key Features
Transparent remote method invocation
Name server for object discovery
Support for callbacks and bidirectional communication
Automatic serialization of Python objects
Files
pyro_server.py - Server hosting the remote object
pyro_client.py - Client accessing the remote object
Setup Instructions
Step 1: Start Pyro4 Name Server
Open a terminal:

python -m Pyro4.naming
Step 2: Start the Pyro4 Server
Open another terminal and navigate to chap6:

python pyro_server.py
Step 3: Run the Client
Open another terminal and run:

python pyro_client.py
Expected Output
Terminal 1 (Name Server):

Not starting broadcast server for localhost.
NS running on localhost:9090 (127.0.0.1)
Warning: HMAC key not set. Anyone can connect to this server!
URI = PYRO:Pyro.NameServer@localhost:9090
Terminal 2 (Server):

Ready. Object uri = PYRO:obj_xxxxx@localhost:xxxx
Terminal 3 (Client):

What is your name? John
Hi welcome John
How It Works
The Name Server acts as a directory service for remote objects
pyro_server.py registers the Server object with the name server
The server object exposes the welcomeMessage method using @Pyro4.expose
pyro_client.py looks up the server using PYRONAME:server
The client calls the remote method transparently
The server processes the request and returns the response
Architecture Diagram
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Client    │────────▶│ Name Server │◀────────│   Server    │
│pyro_client  │  Lookup │  (Registry) │ Register│pyro_server  │
└─────────────┘         └─────────────┘         └─────────────┘
       │                                                │
       └────────────── Direct RPC Call ───────────────▶│
Conclusions
Celery - Distributed Task Queue
Strengths:

Excellent for background job processing and asynchronous tasks
Built-in support for task scheduling and periodic tasks
Robust error handling and retry mechanisms
Horizontal scalability with multiple workers
Supports various message brokers (RabbitMQ, Redis, etc.)
Use Cases:

Email sending and notification systems
Data processing pipelines
Scheduled report generation
Image/video processing
Web scraping and data collection
Long-running computations
Key Takeaway: Celery is ideal when you need to offload time-consuming tasks from your main application and process them asynchronously across distributed workers.

Pyro4 - Python Remote Objects
Strengths:

Transparent remote method invocation (feels like local code)
Easy to implement and understand
Name server for service discovery
Bidirectional communication support
Pure Python implementation
Use Cases:

Distributed computing systems
Microservices architecture
Remote monitoring and control systems
Distributed data processing
Client-server applications
Multi-process coordination
Key Takeaway: Pyro4 excels when you need to distribute Python objects across a network and call their methods remotely while maintaining the simplicity of local object interaction.

Comparison
Feature	Celery	Pyro4
Primary Use	Asynchronous task queue	Remote method invocation
Communication	Message-based (via broker)	Direct object-to-object
Complexity	Higher setup complexity	Simple and straightforward
Scalability	Excellent (multiple workers)	Good (multiple servers)
Task Persistence	Yes (via broker)	No (in-memory)
Scheduling	Built-in support	Manual implementation
Best For	Background jobs	Distributed objects
Final Thoughts
Both Celery and Pyro4 are powerful tools for distributed computing in Python:

Choose Celery when you need a robust task queue with persistence, scheduling, and multiple workers processing jobs asynchronously.

Choose Pyro4 when you need to expose Python objects remotely and want transparent method invocation across a network.

In many real-world applications, these technologies can be combined: use Celery for background task processing and Pyro4 for inter-service communication in microservices architectures.

Further Reading
Celery Documentation
Pyro4 Documentation
RabbitMQ Tutorials
Distributed Systems Concepts