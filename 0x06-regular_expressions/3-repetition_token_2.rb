#!/usr/bin/env ruby
# This script matches string with hb followed
# by one or more occurences of t then n

puts ARGV[0].scan(/hbt+n/).join