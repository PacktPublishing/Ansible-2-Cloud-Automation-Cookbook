# Ansible 2 Automation Cookbook
This is the code repository for [Ansible 2 Automation Cookbook](https://www.packtpub.com/virtualization-and-cloud/ansible-2-cloud-automation-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788295826), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Ansible has a large collection of inbuilt modules for managing various cloud resources. The book starts with the concepts needed to safeguard your credentials and explains how you interact with cloud providers to manage resources. Each chapter begins with an introduction to using the right modules to manage a given cloud provider. The book also includes Amazon Web Services, Google Cloud, Microsoft Azure, and other providers. Each chapter guides you through creating basic computing resources along with other resources that you might use to deploy an application. Finally, you will deploy a sample application to demonstrate various use patterns and utilities for resources.

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
- name: Create Custom Network
  gce_net:
    name: my-network
    mode: custom
    subnet_name: "public-subnet"
    subnet_region: us-west1
    ipv4_range: '10.0.0.0/24'
    state: "present"
    service_account_email: "{{ service_account_email }}"
    project_id: "{{ project_id }}"
    credentials_file: "{{ credentials_file }}"
  tags:
   - recipe1
```

This book assumes that readers are already familiar with the basics of Ansible and the cloud provider they are going to work on. The book helps the readers to write infrastructure as code and automation. Readers will need a way to authenticate and authorize themselves to the desired cloud providers. Usually, that requires creating an account with said cloud provider. Although care has been taken to use trial and free-tier cloud providers wherever possible, certain recipes might cost users a small amount of money. Please be aware of the financial implications of that.

From a hardware point of view, any modern computer running 64-bit Linux flavor will be able to run the recipes. We have run these recipes from a single core 1 GB RAM compute instance.

## Related Products
* [Microsoft System Center Data Protection Manager Cookbook](https://www.packtpub.com/virtualization-and-cloud/microsoft-system-center-data-protection-manager-cookbook-0?utm_source=github&utm_medium=repository&utm_campaign=9781787289284)

* [React Native Cookbook - Second Edition](https://www.packtpub.com/application-development/react-native-cookbook-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788991926)

* [QT5 Python GUI Programming Cookbook](https://www.packtpub.com/application-development/qt5-python-gui-programming-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788831000)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
