# FedoraMessaging
This Repo contains all the files and instructions to get started with Fedora Messaging on Fedora Linux.
# Installation
 1. Firstly, install Fedora Messaging by running the command: `sudo yum install fedora-messaging` 
 2. After Installing fedora-messaging, you need to install RabbitMQ server. Download and install it by running the command: `sudo dnf install rabbitmq-server`
 3. After Installing RabbitMQ Server, enable and start it by running the commands: 
	```
	$ sudo systemctl enable rabbitmq-server
	$ sudo systemctl start rabbitmq-server
	```
 4. (Optional) After Starting RabbitMQ, enable the web UI by running the command: `sudo rabbitmq-plugins enable rabbitmq_management`
 5. (Optional) You can access RabbitMQ Web UI at `localhost:15672` The Username and password is `guest`
# Configuration
After Installing the required software, we need to configure fedora-messaging. You need to first copy the config.toml file in this repo to /etc/fedora-messaging/config.toml. Copy it by running: 
	`cp ./config.toml /etc/fedora-messaging/config.toml`
# Testing the Setup
We can now start our consumer. Open a terminal and run: `python3 ./consumer.py`
This will be listening for messages

Once the consumer is up and running, open another terminal and send a message by running: `python3 ./publisher.py HelloWorld!` This command will send the message "HelloWorld!". You can see it in the outputs of consumer.py
# Further Experiments
 1. You can run Publisher, consumer and RabbitMQ server in different machines and it needs changes in config.toml file. More details can be found [here](https://fedora-messaging.readthedocs.io/en/latest/configuration.html)
# References
 For more info, please refer:
 1. A Simple tutorial I followed: [https://fedora-messaging.readthedocs.io/en/stable/tutorial/index.html](https://fedora-messaging.readthedocs.io/en/stable/tutorial/index.html)
 2. RabbitMQ AMQP concepts: [https://www.rabbitmq.com/tutorials/amqp-concepts.html](https://fedora-messaging.readthedocs.io/en/stable/tutorial/index.html)

