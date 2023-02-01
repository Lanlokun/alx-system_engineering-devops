# 0x05. Processes and signals

# 0. What is my PID


        Write a Bash script that displays its own PID.

<ul>
    ./0-what-is-my-pid
</ul>

# 1. List your processes

    Write a Bash script that displays a list of currently running processes.


<ul>
    ./1-list_your_processes | head -50
</ul>

# 2. Show your Bash PID

    Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

<ul>
    ./2-show_your_bash_pid
</ul>


# 3. Show your Bash PID made easy

    Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

<ul>
    ./3-show_your_bash_pid_made_easy
</ul>

# 4. To infinity and beyond

    Write a Bash script that displays To infinity and beyond indefinitely.

<ul>
    ./4-to_infinity_and_beyond
</ul>

# 5. Don't stop me now!

    Write a Bash script that stops 4-to_infinity_and_beyond process.

<ul>
    ./5-dont_stop_me_now
</ul>

# 6. Stop me if you can

    Write a Bash script that stops 4-to_infinity_and_beyond process.


<ul>
    ./6-stop_me_if_you_can
</ul>

# 7. Highlander

    Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

<ul>
    ./7-highlander
</ul>

# 8. Beheaded process


    Write a Bash script that kills the process 7-highlander.

<ul>
    ./7-highlander
    (open another terminal)
     ./8-beheaded_process
</ul>

# 9. Process and PID file


    Write a Bash script that:

    Creates the file /var/run/myscript.pid containing its PID
    Displays To infinity and beyond indefinitely
    Displays I hate the kill command when receiving a SIGTERM signal
    Displays Y U no love me?! when receiving a SIGINT signal
    Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

<ul>

    ./100-process_and_pid_file

</ul>

# 10. Manage my process


    Write a manage_my_process Bash script that:

    Indefinitely writes I am alive! to the file /tmp/my_process
    In between every I am alive! message, the program should pause for 2 seconds
    Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)

    Requirements:

    When passing the argument start:
    Starts manage_my_process
    Creates a file containing its PID in /var/run/my_process.pid
    Displays manage_my_process started
    When passing the argument stop:
    Stops manage_my_process
    Deletes the file /var/run/my_process.pid
    Displays manage_my_process stopped
    When passing the argument restart
    Stops manage_my_process
    Deletes the file /var/run/my_process.pid
    Starts manage_my_process
    Creates a file containing its PID in /var/run/my_process.pid
    Displays manage_my_process restarted
    Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed
    
<ul>
    ./101-manage_my_process
</ul>

# 11. Zombie


    Write a C program that creates 5 zombie processes.

<ul>
    gcc 102-zombie.c -o zombie
    ./zombie 
    (open another terminal)
    ps aux | grep -e 'Z+.*<defunct>'
</ul>
