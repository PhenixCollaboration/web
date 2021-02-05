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

##### ROOT
###### Running the latest version of ROOT is a one-liner
A large number of PHENIX analysis have been done with ROOT versions 5.\*. For example,
in early 2021 ROOT version 5.34.36 was in use on interactive nodes of BNL SDCC. Using a consistent
version of ROOT may be important for reproducibility of analyses and other purposes. Instructions
for **running ROOT5 using Docker** will be given in sections below.

However, assuming the user needs to run *the most current version* of ROOT on a Docker-equipped
machine it is rather straightforward:
```bash
docker run -it --rm rootproject/root root
```
In this example, Docker will find the required *ROOT image* in the remote
repository (e.g. Docker Hub), download it automatically, add it to the local cache and then
start a container which proceeds to invoke the "root" command, at which point the user is
presented wtih the usual ROOT prompt. The '*-it*' option instructs Docker to run an interactive
shell connected to the container, and '*\-\-rm*' is a cleanup option which makes it easier
to manage your Docker environment but is not critical.

###### Caveats
1. In the example above, ROOT will indeed run interactively -- in the command line mode --
but likely without graphics. If the graphics capability is needed additional settings
are required as detailed in the *"X11"* section below.
2. In most cases, to use ROOT meaningfully one typically needs to exchange files between
the host (your machine) and the container process. This may include input and output data
as well as ROOT macros. It doesn't happen by default -- since containers run in isolation --
so sharing of folders ("volumes") has to be set up explicitely> Fortunately, this is
straightforward and is explained in the *"Volumes"* section below.

###### X11
To enable container access to the X11 server on your machine the *xhost* permissions need
to be set. The easiest (but not very secure) way of doing this is as follows:
```bash
xhost +
```
Utilizing the X11 graphics capability entails the use of command-line
options which define proper security settings, interprocess communication mode etc.
Below is a working example tested on Ubuntu 18.04:
```bash
docker run -it --ipc=host --rm -e DISPLAY=$DISPLAY --security-opt="label:disable" -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root root
```
Once run, this command presents the user with the ROOT prompt and the graphics mode will be active, however
there won't be the usual ROOT splash screen at start-up. At the prompt, the usual TBrowser, canvas and
other graphics tools can be invoked as needed.

###### Volumes
There are several ways to achieve that, cf.
{% include_cached navigation/findlink.md name='docker_volumes' tag='Docker documentation on volumes' -%}.

