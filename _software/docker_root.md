---
name: docker_root
layout: newbase
---
<h3>Running ROOT in Containers</h3>

* TOC
{:toc}
##### Overview

This page was created as a quick reference for running different versions
of ROOT in Docker containers. For technical details and reasons to use various
command line options please see the
{% include navigation/pagelink.md folder=site.analysis name='docker' tag='"Docker technical notes"'%} page.

The PHENIX Collaboraiton published a small selection of Docker images on
{% include navigation/findlink.md name='docker_hub' tag='Docker Hub' %} for everyone's use. For that
reason, running both the most recent version of ROOT and the preserved/legacy version of ROOT via Docker
containers is pretty much identical.

##### Accessing ROOT Images
The following assumes that the user has installed Docker on their machine.
```bash
# To run the current verion of ROOT - which is ROOT6 at the time of writing:
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root

# To run ROOT5 preserved as a Docker image:
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix phenixcollaboration/tools:sl7_root5
```
Since typing a long command like this may be tedious and error-prone one can easily define an
*alias* in any Linux-like environment e.g.
```bash
# create the alias which works for any X11-capable container:
alias droot='docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix '

# Run the ROOT5 container based on the PHENIX image
droot phenixcollaboration/tools:sl7_root5
```
Of course the whole command including the name of the image can be aliased just as easily.
Creating shell functions and/or scripts is equally easy and will be a functional equivalent
of commands like this one, while having more flexibility. For example, one can conveniently
define *different* volumes to be mounted, as necessary - see the section below.

##### Sharing files between the host and the container
In order to share the filesystem between the host machine and the Docker container one
needs to use the "-v" option as explained on the
{% include navigation/pagelink.md folder=site.analysis name='docker' tag='"technical notes"'%} page.
For example, if the user has created a Docker volume called "myvolume" (and potentially
populated is with data on the local host) it will be accessible in the ROOT5 container as the "/user"
folder if the following command is used (and assuming the '/user' folder is defined in the image):
```bash
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix -v myvolume:/user phenixcollaboration/tools:sl7_root5
```
The command explicitly maps the Docker volume "myvolume" defined in the Docker system on the *host*,
to the "/user" folder that will be instantiated in the running container based on the definition
in the image.
If a command such as this one is used repeatedly it might be a good idea to create aliases similar to one descibed
in the previous section.

##### Shell access to a running container
In order to gain shell access to the container instead of jumping into ROOT one
needs to simply add "bash" to the end of the command line i.e.
```bash
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix -v myvolume:/user phenixcollaboration/tools:sl7_root5 bash
```
This will start the bash shell which will function normally. This may be necessary to check presence of requisite
files, macros and other settings. Starting ROOT is still possible of course by using the "root" command from that shell.
