---
name: docker
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
##### Overview
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

This page is not meant to serve as a Docker tutorial or a reference, in
particular because of plentiful and helpful documentation easily available on the Web.
Instead it contains select instructions and examples which will be hopefully helpful to
users wishing to leverage the capabilities of Docker for practical
applications in PHENIX and elsewhere.
It is recommended that new users consult the main
{% include_cached navigation/findlink.md name='docker' tag='Docker documentation page' %}
for orientation, introduction, tutorials and as a general reference. Consider going
through 
{% include_cached navigation/findlink.md name='docker_101' tag='Docker tutorials' -%}.
**Docker can be easily installed on any Linux machine**, and in addition to that
there is a "
{%- include_cached navigation/findlink.md name='docker_desktop' tag='desktop application' -%}"
available for Linux, Windows and MacOS. Examples and tutorials can even be
{% include_cached navigation/findlink.md name='docker_play' tag='run in the cloud' %}
without the need to install any software on your machine.

An important part of every Docker development and workflow is a *registry* which serves
as a storage and catalog of Docker *images*. A registry can be hosted locally or
exist as a cloud service. A prominent cloud platform serving that purpose is
{% include_cached navigation/findlink.md name='docker_hub' tag='Docker Hub' -%}.

The following examples assume that Docker has been installed on the system.
{{ site.hr }}
##### Running the latest version of ROOT is a one-liner
*The most current version of ROOT* can be run on a Docker-equipped machine
with one command -- no additional installation(s) required:
```bash
docker run -it --rm rootproject/root root
#
# The '-it' option instructs Docker to run an interactive  shell connected to the container;
# '--rm' is a  cleanup option for your Docker environment and is not critical.
```
In this example, Docker will locate the required *ROOT image* in the remote
repository (e.g. Docker Hub), download it automatically, add it to the local
cache and then start a *container process*. That process then proceeds to invoke
the "root" command as specified on the command line. At this point the user is
presented wtih the usual ROOT prompt.
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
software compatibility. Specific instructions for **running ROOT5 using Docker** are given in the
*"ROOT5"* section below.
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
##### Windows
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
{{ site.hr }}
##### ROOT5
*Work in progress*

