---
name: docker
layout: newbase
---
{% include layouts/find_title.md name=page.name %}
##### Overview
Docker is OS-level virtualization platform which allows complete software
packages to run in isolation while utilizing the same kernel as the host
operating system. This is the key distinction between Docker and the Virtual
Machine technology which involves an entire level of emulation run on top
of the host OS. A running instance of software managed by Docker is called
a *container*, while the read-only template used to instantiate it is termed
an *image*. This technology makes it possible to capture a complete
software environment which includes a specific flavor of Linux chosen
by the developer and all the necessary libraries and dependencies in
a self-contained, portable package which can be run on any machine where
Docker is installed. One of the motivations to consider Docker is its
central role in the framework for reproducible analysis:
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
It is straightforward to run the most current version of ROOT on a Docker-equipped machine:
```bash
docker run -it --rm rootproject/root root
```
However note two issues to keep in mind when running this command:
1. In the example above, ROOT will run interactively but without graphics. This may or may not
be a problem depending on the situation.
2. By default containers run in isolation from each other and the host machine,
which includes a completely separate file system.
To use ROOT meaningfully one typically needs meaningul exchange of data between the host
and other systems, and the container. For that to happen, sharing of folders
("volumes") has to be set up. There are several ways to achieve that, cf.
{% include_cached navigation/findlink.md name='docker_volumes' tag='Docker documentation on volumes' -%}.

Utilizing the X11 graphics capability entails the use of command-line
options which define proper security settings, interprocess communication mode etc.
Below is a working example tested on Ubuntu 18.04:
```bash
docker run -it --ipc=host --rm -e DISPLAY=$DISPLAY --security-opt="label:disable" -v /tmp/.X11-unix:/tmp/.X11-unix rootproject/root root
```
Once run, this command presents the user with the ROOT prompt and the graphics mode will be active, however
there won't be the usual ROOT splash screen at start-up. At the prompt, the usual TBrowser, canvas and
other graphics tools can be invoked as needed.
