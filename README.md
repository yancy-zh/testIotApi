# A simple framework for tests with IOT API

This is a project to enable the basic automated tests for the IOT based API functionality as you have a server on your local machine or remotely. Here, the test framework is built on a server template, powered and published by [Directus](https://docs.directus.io), a complete suite of for API definition, endpoints and repository
 for a typical IOT ecosystem. The features presented in this software include both static and dynamic objects that are 
 commonly used in the IOT oriented web services. 
 
## Prerequisites
The following instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
To acquire the basic environment for setting up a server that hosts websites and web apps, use LAMP stack. To install and
 test out the functions of this framework, a test server that includes the basic structure of Directus 
should be installed in advance. The test framework as well as the test cases presented in this repository, is based on Directus software and its database, 
so this template is only meaningful, functioning and necessary to be imported when Directus is installed. 

### LAMP stack
Since this Directus is just a sample server as the other web applications running as a virtual host, it depends on the basic server environment.
  Typically, a LAMP stack, which is a standard combination of open-source software, is used for setting
   up this host environment. This group of basic server related components, are commonly referring to:
* Linux operating system (a popular version of which is [Ubuntu](https://ubuntu.com/))
* [Apache web server](https://httpd.apache.org/) (a version of which is Apache2)
* [MySql database management](https://www.mysql.com/)
* [PHP content processing](https://www.php.net/)

The best way to setup the environment is to follow the [official instruction provided on Directus documentation pages](https://docs.directus.io/getting-started/installation.html),
where four methods for installing Directus are described. As a result, you will obtain a local copy of Directus (API and its databases). 
I personally have followed the [installation instruction using Git](https://docs.directus.io/installation/git.html) to 
set up my Directus virtual host. Besides, the most helpful, illustrative and well organized resources that I found and used are 
  * [Install and configure Apache web server on Ubuntu](https://vitux.com/how-to-install-and-configure-apache-web-server-on-ubuntu/)
  * [How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)
  * [How to setup Apache, MySql, and PHP on Ubuntu Linux](https://www.youtube.com/watch?v=TrLAx27Npns) 
 
### Directus
 The information needs to be read is mainly the official website of [Directus](https://docs.directus.io),
 the [Directus Github respository](https://github.com/directus/api) and 
the [documentation](https://docs.directus.io/getting-started/introduction.html#what-is-directus) regarding this software suite.

For installation, use instructions listed under [Installation page](https://docs.directus.io/getting-started/installation.html) 
and [trouble shooting page](https://docs.directus.io/getting-started/troubleshooting.html). The [community](https://github.com/directus/directus/issues) also contains abundant 
tricks and solutions that are helpful for installation.  

For understand the available API definition and endpoints, use the [API reference](https://docs.directus.io/getting-started/troubleshooting.html). 
 
### Python 3
Python 3 is used when this project is constructed. This project requires the following packages to be installed:
  * requests
  * unittest
  * json
  * datetime
  
Python 3 can be acquired at the [official website](https://www.python.org/), download page. 
 To check which packages have already been installed in your python 3 environment, you can run the following command in your
 shell or powershell terminal:
 ```
python3 freeze
```
### Verification of the installation for dependencies
As a validation of the above mentioned Prerequisites having been satisfied, you should be able to see
* A url pointing to the virtual host on your local machine, if the server is. For example, if typing the address:
```
localhost
```
you should see the installation page:
```
localhost/admin/#/install/
```
![installation_page_of_directus_project](https://user-images.githubusercontent.com/60941643/82092533-c12a0100-96f9-11ea-9b30-29fe016e3323.png)

* A virtual host named 'directus' is established, which appears as a directory with the same name in the domain 
management folder '/var/www/' in Linux system. In the directory 'directus', folders such as 'src', 'bin', 'config' should show.
* After a Directus project is created, when accessing the IP of your local host, which is usually http://HOST_IP, the
 apache server will be redirecting you to the Directus application login page 'http://HOST_IP/admin/#/login'
 ![Login page of directus project](/resource/login page of directus project.png)
* A project in Directus which you can login with the admin user you have defined
* The python 3 environment with packages listed in Prerequisites and a Python IDE

## Install the test framework for IOT API
1. Clone the repository of this project to your local machine.
2. Modify the configuration file located in '/config' directory. It should contain the authentication information, 
project name as well as the HOST_IP of your test server. 
3. It should be noted that, the dummy information that are shared by multiple test cases, can be defined as a test base 
and should be listed in the configuration file, such as fake collection IDs, fake user names. 

## Running the tests

If unit tests are used for running the tests, use the module name for the configuration file. 

## Author

* **Yao Zhang** - *Initial work* - [yancy-zh](https://github.com/yancy-zh)

## Acknowledgments
* Directus


