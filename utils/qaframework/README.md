Goal of this is to write a tool, `answer`, that people can use for ssh challenges to answer a couple of questions and get a flag only when every question is answered.

The tool will assume a directory in /tmp/qaframework, owned by root:user, with permissions 730. This ensures write access but no list access. This part must be baked into the Dockerfile for the ssh challenge.

To build a copy of the tool with the right challenges, use `build.py config.py outputfolder`. This will put the final `answer` binary and its dependencies into outputfolder, which should be copied into `/usr/local/bin/` in the Docker container.

Don't forget to change the `answer` binary to mode 111 (only executable)!
