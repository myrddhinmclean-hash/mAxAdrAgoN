---
title: "A Folder That Runs My Computer"
date: "2026-08-31"
hoard: "machine"
summary: "The dumbest possible way to let an assistant in the cloud do things on a machine it cannot reach: drop a script in a folder and let a loop find it. No daemon, no API, no open port."
---

# A Folder That Runs My Computer

An assistant running in a data centre cannot touch this machine. It has no shell here, no port, no agent installed. The usual answer to that is a chat window full of commands and a person copying them into a terminal one at a time, which is the whole problem wearing a solution costume.

The fix is a folder.

A small PowerShell loop watches a queue directory. When a script appears in it, the loop runs it and moves it to a done directory. That is the entire mechanism. The assistant writes a file, waits, and reads whatever the script wrote to disk. No daemon to install, no port to leave open, nothing listening for a connection, and no credential anywhere that a network can reach.

The security property falls out of the shape rather than being added on. Nothing accepts a connection, so nothing can be connected to. The only way in is writing a file into one specific folder, and the only things that can write there are things already trusted with the disk.

What it cost was a set of specific, unglamorous lessons, each learned by something failing:

**Output goes to a file, never the console.** Anything else is unreadable from the far end. Every script's first act is opening a text file to write into.

**ASCII only.** An em-dash inside a quoted string killed a script with a parse error that pointed at a line thirty rows away from the actual problem. The reported error location was useless. The rule now is that no script contains a character a 1980s terminal would refuse.

**Python for anything structural.** PowerShell's handling of JSON is unreliable enough that every script needing to read or write structured data shells out to Python instead.

**Check the exit code, and check the right one.** Git writes its progress to the error stream, so a successful push renders in red and looks like a crash. Worse, reading the exit status after piping through a file writer returns the writer's status rather than the program's, which produced a test that reported four passes when nothing had run at all. That mistake got made twice, the second time after it had already been written down.

The thing I did not expect was how much the queue changes the shape of a session. Work stops being a conversation about what should happen and becomes a sequence of things that did. Write the script, wait forty seconds, read the result, decide. A person is still deciding, but they are deciding on evidence from their own machine instead of on a plan.

Roughly thirty scripts went through it in one night: a repository moved off a syncing drive by fresh clone, a validator tested against a deliberately broken index, an embedding model installed and calibrated, four site sections built and pushed.

Not one command was pasted into a terminal.
