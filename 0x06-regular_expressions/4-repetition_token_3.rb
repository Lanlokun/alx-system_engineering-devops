#!/usr/bin/env ruby
# This script matches a string with hb
# followed by 0 or more occurences
# of t then n

puts ARGV[0].scan(/hbt*n/).join