#!/usr/bin/env ruby
# This script takes an argument
# and pass it to a regex for
# repetition token

puts ARGV[0].scan(/hbt{2,5}n/).join