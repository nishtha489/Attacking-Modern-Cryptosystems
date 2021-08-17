#!/usr/bin/expect

spawn ssh student@65.0.124.36
expect "password"
send "caesar\n"
expect "*WELCOM*"
send "AlphaBeta\n"
expect "*pass*"
send "hamsandhash\n"
expect "level"
send "5\n"
expect "> "
send "go\n"
expect "> "
send "wave\n"
expect "> "
send "dive\n"
expect "> "
send "go\n"
expect "> "
send "read\n"

set f1name "input.txt"
set f1 [open "$f1name" r]
set input_file [read $f1]

# set f2name "output.txt"
# set f2 [open $f2name "w"]

# make sure that output.txt doesn't exist otherwise it will append to it
log_file output.txt
 
foreach line $input_file { 
  expect "> "
  send "$line\r"
  expect "Press c to continue> "
  send "c\r"
}

close $f1
# close $f2

expect "*> "
send "back\r"
expect "*> "
send "exit\r"