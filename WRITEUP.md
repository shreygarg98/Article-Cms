# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*


| | VM  |  App service|
| - | - | - |
| Type of resource| **Infrastructure as a service**: more things to manage, install and take care of. |  **Platform as a service**: Another level of abstraction for a better user experience.|
| Costs per month | For a Basic tier 2 GB RAM, 1 core, 10 GB storage 500 MXN | 1.75 GB RAM, 1 core, 10 GB storage 1000 MXN, this is more expensive, you have to do less work, it makes sense|
| Scalability | Yes | Yes |
| Workflow | More work on your side, not necesarilly harder, but it will certainly take more time, steps or maintenance. | Easier, specialized |
| Availability| Traffic manager by azure | Traffic manager by azure |


Here our major task is to have the web app running, an app service is the best solution because we don't need to worry about the environment that it's running on and we need toamnage all the updates and infrastructure.We have a web app that is deployed to azure using Aure pipelines with github and so It is much better than Virtual Machine although cost is greater but still acceptable.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

* The app service is used by me to integrate it with a python web app already created so I integrated it with github and task was done easily. If I have to code python app, then may be I could use VM.

* Suppose I have to change more things on the web server,then maybe the VM is not the only choice,I could use a container solution, where the web server is a separate service from the web app itself.

* A VM offers more flexibility, but has some bad practices.Suppose a microservice architecture is in place,then there are other azure solutions that will give you more reliability.

* A VM could be a good option but still in our case App service is better.