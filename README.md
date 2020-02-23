# web-calculator-project
Repository for web calculator project for Cloud Computing module.

Objective:
The objective of this project was to create a functioning online calculator hosted on an internal private cloud - QPC (Queen's Private Cloud). The calculator itself consisted of a number of mathematical functions that were individually incorporated into separate microservices.
Each of these services were implemented in different languages, with 6 functions in total, implemented in Python, NodeJS, PHP, Java and Go. The services were then packaged into Docker containers with appropriate Docker images for their respective language of implementation.

Front end and mathematical microservices:
The calculator was hosted on a front end made up of HTML and various Javascript functions to get user input, call the microservices from their respective URL's and capture JSON output from the services and display it to the user. The front end also has various error and exception handling implemented.
The front end along with all of the mathematical microservices were hosted on individual kubernetes clusters with load balancing included in the form of ingress and egress controllers.

Proxy router microservice:
For maximum availability and mitigate any SPOF's (Single points of failure), a proxy router microservice was created that acted as a proxy between the front end and the mathematical functions. The proxy itself was hosted on a separate kubernetes cluster with load balancing and availability with the addition of multiple pods on the cluster. In the final release of the calculator all of the traffic from the front end was routed through the proxy to the backend microservices vice versa.

Monitoring microservice:
A monitoring microservice was also implemented in the aim of providing monitoring of the whole system as well as some performance statistics. A metric that was used for measuring the performance of the system was the response time from the function microservices. This response time was a useful metric in determining the performance of the calculator and for the specific services. This service was hosted on its own cluster.

Ci/CD Testing:

Unit Testing:
