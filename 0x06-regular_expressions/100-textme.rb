#!/usr/bin/env ruby
# Script outputs: [SENDER], [RECEIVER], [FLAGS]
# Sender's phone number/name
# Receiver's phone number/name
# Flags used

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')