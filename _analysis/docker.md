---
name: docker
layout: newbase
---

<h3>Docker</h3>
* TOC
{:toc}

##### About this page

**This page is not meant to serve as a Docker tutorial or a reference**, in
particular because of abundance of helpful documentation easily available on the Web.
Presented here are select instructions and examples which will be hopefully helpful to
beginners wishing to leverage the capabilities of Docker for practical
applications in PHENIX and other experiments.
It is recommended that new users consult the main
{% include_cached navigation/findlink.md name='docker' tag='Docker documentation page' %}
for orientation, introduction and general reference. Consider going
through some of the 
{% include_cached navigation/findlink.md name='docker_101' tag='Docker tutorials' -%}.

For quickstart instructions on how to take advantage of
running different versiond of ROOT in Docker containers please see the
{% include navigation/pagelink.md folder=site.analysis name='docker_root' tag='"Running ROOT in Containers"' %} page.

##### What is Docker?
Docker is a OS-level virtualization platform which allows complete software
packages to run in isolation while utilizing the same kernel as the host
operating system. This is the key distinction between Docker and the Virtual
Machine technology which involves an entire level of emulation run on top
of the host OS. A running instance of software managed by Docker is called
a *container*, while the read-only template used to instantiate it is termed
an *image*. This technology makes it possible to capture the complete
software environment including a specific flavor of Linux chosen
by the developer, compiled user code and all the necessary libraries and
dependencies in a self-contained, portable package which can be run on any
machine where Docker is installed. One of the motivations to consider Docker
is its central role in the framework for reproducible analysis -
{% include navigation/pagelink.md folder=site.analysis name='reana' tag='REANA' -%}.

**Docker can be
{% include_cached navigation/findlink.md name='docker_install' tag=' easily installed ' %}
on any Linux machine** (exact method will depend on the Linux distribution), and in addition
to that there is a "
{%- include_cached navigation/findlink.md name='docker_desktop' tag='desktop application' -%}"
available for Linux, Windows and MacOS. Examples and tutorials can even be
{% include_cached navigation/findlink.md name='docker_play' tag='run in the cloud' %}
without the need to install any software on your machine.
An important part of every Docker development and workflow is a *registry* which serves
as a storage and catalog of Docker *images*. A registry can be hosted locally or
exist as a cloud service. A prominent cloud platform serving that purpose is
{% include_cached navigation/findlink.md name='docker_hub' tag='Docker Hub' -%}.

The following examples assume that Docker has been installed on the system.
The docker daemon runs as *root* so all docker commands will need to be run via *sudo*.
However, this can be avoided by adding users to a special *docker* group according
to the instructions found on the Docker
{% include_cached navigation/findlink.md name='docker_post_install' tag='"post installation steps"' %}
page.

It is also possible to run Docker images using the 
{% include_cached navigation/findlink.md name='singularity' tag='Singularity' %}
containerization framework. Please see relevant Singularity documentation pages
for details. Brief notes on how to do this on the interactive
{% include_cached navigation/findlink.md name='sdcc' tag='SDCC' %}
nodes at BNL
can be found on the 
{% include navigation/pagelink.md folder=site.analysis name='docker_root' tag='"Running ROOT in Containers"' %}
page.

{{ site.hr }}
##### Running the latest version of ROOT is a one-liner
*The most current version of ROOT* can be run on a Docker-equipped machine
with one command -- no additional installation(s) required.
In this example, Docker will locate the required *ROOT image* in the
registry (e.g. Docker Hub which is usually the default), download it automatically,
add it to the local cache and then start a *container process*. That
process then proceeds to invoke the "root" command as specified on
the command line. In the following command, the *'-it'* option instructs
Docker to run an interactive  shell connected to the container,
and the *'--rm'* is a  cleanup option for your Docker environment
(it is not critical for operation of the container itself).

```bash
docker run -it --rm rootproject/root root  #  The user is presented wtih the usual ROOT prompt.
```
{{ site.hr }}
##### Caveats
1. In the example above, ROOT will indeed run interactively -- in the command line mode --
but likely without graphics. If the graphics capability is needed additional settings
are required as detailed in the *"X11"* section below.
2. In most cases, to use ROOT meaningfully the operator typically needs to exchange
files between the host (your machine) and the container process. This may include input
and output data as well as ROOT macros. It doesn't happen by default
-- since containers run in isolation --
so sharing of folders ("volumes") has to be set up explicitely> Fortunately, this is
straightforward and is explained in the *"Volumes"* section below.
3. A large number of PHENIX analysis have been done with ROOT versions 5.\*. For example,
in early 2021 ROOT version 5.34.36 was in use on interactive nodes of BNL SDCC. Using a consistent
version of ROOT may be important for reproducibility of analyses and other purposes e.g. to ensure
software compatibility. Specific instructions for **running ROOT5 using Docker** are given on the
{% include navigation/pagelink.md folder=site.analysis name='docker_root' tag='"Running ROOT in Containers"'%} page.
4. Platorm dependency - this is not a large issue but certain host systems may require
extra runtime settings, see the *Windows* section below for an example.
{{ site.hr }}
##### X11
###### Server access
To enable container access to the X11 server on your machine requisite permissions need
to be set. The easiest (but not very secure) way of doing this is as follows:
```bash
xhost +
```
###### Shared memory access
Some versions of the X11 server software require shared memory access
for optimal performance, which may get in the way of proper graphics
functionality of containers. This can be addressed in two different ways:
1. Using the "ipc" option at runtime to enable interprocess communication between
the container and the X11 server -- theoretically, this will result in better performance.
2. Disabling the shared memory mode of operation.

Which version is best will depend on the needs of the user so some testing is
recommended. Shown below are examples illustrating both options -- either one should
provide full graphics capability e.g. the usual TBrowser, canvas and other
graphics tools.

```bash
# Note proper security settings in both example.
# Examples tested on Ubuntu 18.04
#
# 1. Interprocess communication enabled, shared memory mode implied.
# NB. with this option the usual ROOT splash screen at start-up won't be shown.
docker run -it --ipc=host --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root root
#
# 2. Shared memory functionality is disabled.
docker run -it  --rm -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root root
```
{{ site.hr }}
##### Microsoft Windows
There is an option *\-\-security-opt* which is currently meaningful in the
Windows environment only and may be needed for proper operation.
```bash
# Please refer to Docker documentation for other details of the Windows environment.
# This command corresponds to the example above which disables the X11 memory sharing.
docker run -it  --rm -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 --security-opt="label:disable" -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root root
```
{{ site.hr }}

##### Volumes
There are several ways to achieve sharing of volumes i.e. establishing storage area accessible from both
the host and the container(s) running on the host. For detailed information, please see 
{% include_cached navigation/findlink.md name='docker_volumes' tag='Docker documentation on volumes' -%}.
In the following, a basic example of utilizing volumes is presented, using just one method of several
available. Let us assume that the image used to instantiate a container was created with a Dockerfile
containing a directive similar to the following:
```dockerfile
WORKDIR /user
```
A container (i.e. a running process) instantiated from this image will then have a directory named
"/user" which is entirely internal to that container i.e. inaccessible from the host system.
Now, let us assume that the operator issues the following command:
```bash
docker volume create myvolume
```
This results in the creation of a *Docker volume* which is mapped to a specific location
in the filesystem of the host machine. The exact name chosen for the volume is immaterial.
To determine the location to which the volume is napped the following command can be used:
```bash
docker volume inspect myvolume
```
...which will result in an output similar to:
```json
[
    {
        "CreatedAt": "2021-02-06T20:10:06-05:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/myvolume/_data",
        "Name": "user",
        "Options": {},
        "Scope": "local"
    }
]
```
The content of the volume will be kept in the directory pointed to by the "Mountpoint" attribute
in the JSON output above. This directory is owned by *root* so access (including operations like "ls")
will only be possible using the root account or via sudo. Since the volume was just created it won't
have any content yet:
```bash
$ sudo ls -l /var/lib/docker/volumes/myvolume/_data
total 0
```

Note that at this point the volume is unrelated to any specific Docker image and/or container.
To establish binding of the volume to the container filesystem an option should be added to the "docker run command",
as in the following command line:
```bash
# Running a ROOT5 image parepared by the PHENIX Collaboration
docker run -it --ipc=host --rm  -v /tmp/.X11-unix:/tmp/.X11-unix -v myvolume:/user phenixcollaboration/tools:sl7_root5
```

##### Custom folders and other customization
In the example above, the image used to instantiate the ROOT5 container has an internal folder "/user" defined.
This is because the
{% include_cached navigation/findlink.md name='github_docker_sl7_root5' tag='**Dockerfile**' %}
used to create this image contained the requisite instruction
```dockerfile
WORKDIR /user
```
There is nothing special about the "/user" name for this folder. Any names can be used and any folder hierarchy can
be created to better suit the needs of the user's work. It is not difficult to build customized images based on examples
contained in the respective 
{% include_cached navigation/findlink.md name='github_docker_sl7' tag='PHENIX GitHub repository'-%}. One can modify
the Dockerfile and run the build locally, however be aware that a complete Docker build of ROOT will take a while.
Alternatively, as a faster alternative, one can create a *customization layer* on top of an image already pushed to 
{% include navigation/findlink.md name='docker_hub' tag='Docker Hub'-%}. The "base" ROOT5 image can be obtained
and committed to local storage on the user's machine by ising the command
```bash
docker pull phenixcollaboration/tools:sl7_root5
```

##### Singularity
Docker images can also be used within the
{% include_cached navigation/findlink.md name='singularity' tag='Singularity' %}
containerization framework. It has been deployed on SDCC nodes at BNL and is available
by any user. For example, to start the SL7/ROOT5 image created by the PHENIX Collaboration
and get to the *bash* prompt the following command can be used:
```bash
singularity exec --bind /phenix/u/phnxuser:/user docker://phenixcollaboration/tools:sl7_root5 bash
```
In this example, the home directory of the user "phnxuser" will be mapped to the folder '/user' which
was defined in the image *sl7_root5*. For more detail please see information on folders presented above.

Although ROOT can be started without invoking the shell first as it is the default command in the image,
in this case this will be necessary to explicitly set the *DISPLAY* variable so that X11 tunneling properly
works and X11 functionality is available.
First, one determines the setting on the interactive node in use, which may look like
```bash
$ echo $DISPLAY
localhost:15.0
# actual value will vary
```
Then, after invoking the "singularity exec" command as presented above, the user needs to
set the environment variable accordingly by using the shell within the container:
```bash
$ export DISPLAY=localhost:15.0
```
At that point, applications like xterm, emacs etc will properly function via X11.
And, since this image also contains ROOT5, it can be invoked by typing "root"
and will have the graphics capability.
