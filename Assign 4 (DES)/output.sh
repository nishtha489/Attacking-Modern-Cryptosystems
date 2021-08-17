
#!/usr/bin/expect -f

spawn ssh student@65.0.124.36
expect "password"
send "caesar\n"
expect "groupname"
send "AlphaBeta\n"
expect "pass"
send "hamsandhash\n"
expect "level"
send "4\n"
expect "command"
send "read\n"
# expect "key"
# send "password\n"

set f1name "input.txt"
set f1 [open "$f1name" r]
set input_file [read $f1]

set f2name "output.txt"
set f2 [open $f2name "w"]

foreach line $input_file {
  expect "> "
  send "$line\r"

  expect "$line\r"
  expect "Slowly, a new text starts appearing on the screen. It reads ..."
  expect "\n\t\t*\n"
  puts -nonewline $f2 "$expect_out(0,string)\n"

  expect "Press c to continue> "
  send "c\r"
}

close $f1
close $f2

expect "*> "
send "back\r"
expect "*> "
send "exit\r"
