#! /usr/bin/env python3

import os, sys, time, re
PS1 ="$ "
while True:
    instruction = input(PS1)
    if instruction.lower() == "exit":
        break
    inst1 = instruction.split(" ")
    try:
        if inst1[1] == "PS1":
            PS1 = inst1[3].replace("\"","")
            continue
    except IndexError:
        pass

    pid = os.getpid()               # get and remember pid

    os.write(1, ("About to fork (pid=%d)\n" % pid).encode())

    fds = os.pipe()
    os.set_inheritable(fds[0], True) #4 read
    os.set_inheritable(fds[1], True) #3 write

    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:                   # child
        os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
        
    
        if len(inst1) != 1 and '|' != inst1[1]:
            if '<' == inst1[1]:
                temp = inst1[0]
                inst1[0] = inst1[2]
                inst1[2] = temp
    
    
                os.close(1)                 # redirect child's stdout
                sys.stdout = open(inst1[2], "w")
                fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
                os.set_inheritable(fd, True)
                os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())
    
        elif len(inst1) != 1:
            os.close(1)
            os.dup(fds[1])
            os.close(fds[0])
            os.close(fds[1])
            os.set_inheritable(1, True)
            sys.stdout = os.fdopen(1, "w")
    
        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, inst1[0])
            try:
                os.execve(program, inst1, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly 

        os.write(2, ("Child:    Error: Could not exec %s\n" % inst1[0]).encode())
        sys.exit(1)                 # terminate with error

    rc2 = -1
    try:
        if '|' == inst1[1]:
            rc2 = os.fork()
    except IndexError:
        pass
    if rc2 == 0:
        os.write(1, ("Child: My pid==%d. Parent's pid=%d\n" % (os.getpid(), pid)).encode())
        
        os.close(0)
        os.dup(fds[0])
        os.close(fds[0])
        os.close(fds[1])
        os.set_inheritable(0, True)
        sys.stdin = os.fdopen(0, "r")
    

        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, inst1[2])
            try:
                os.execve(program, inst1, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly 

        os.write(2, ("Child:    Error: Could not exec %s\n" % inst1[2]).encode())
        sys.exit(1)                

    else:                           # parent (forked ok)
        os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % (pid, rc)).encode())
        os.close(fds[0])
        os.close(fds[1])
        childPidCode = os.wait()
        try:
            os.wait()
        except ChildProcessError:
            pass
        os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                 childPidCode).encode())
