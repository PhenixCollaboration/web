---
name: docker_root
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
##### Overview

This page was creates to serve as a quick reference for running different versions
of ROOT in Docker containers. For technical details and reasons to use various commans line
options please see the
{% include navigation/pagelink.md folder=site.analysis name='docker' tag='"Docker technical notes"'%} page.

The PHENIX Collaboraiton published a small selection of Docker images on
{% include navigation/findlink.md name='docker_hub' tag='Docker Hub' %} for everyone's use. For that
reason, running the most recent version of ROOT and the preserved/legacy version of ROOT via Docker
containers is pretty much identical.

##### Running ROOT Containers
The following assumes that the user has installed Docker on their machine.
```bash
# To run the current verion of ROOT - which is ROOT6 at the time of writing:
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root
# To run ROOT5 preserved as a Docker image:
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix phenixcollaboration/tools:sl7_root5
```

In order to share the filesystem between the host machine and the Docker container one needs to use
the "-v" option as explained on the
{% include navigation/pagelink.md folder=site.analysis name='docker' tag='"technical notes"'%} page.
For example, if the user has created a Docker volume called "myvolume" (and potentially
populated is with data) it will pop up in the ROOT5 container as the "/user" folder if the following command
is used:
```bash
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix -v myvolume:/user phenixcollaboration/tools:sl7_root5
```

##### Shell access
In order to gain shell access to the container instead of jumping into ROOT one
needs to simply add "bash" to the end of the command line i.e.
```bash
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix -v myvolume:/user phenixcollaboration/tools:sl7_root5 bash
```
This will start the bash shell which will function normally. This may be necessary to check presence of requisite
files, macros and other settings. Staring ROOT is still possible of course by using the "root" command from that shell.
