#!/usr/bin/ruby

threads = []
for i in 1..100 do
    puts "Creating thread #{i}"
    threads << Thread.new(i) do |j|
        sleep 1
        puts "Thread #{j} done"
    end
end
puts "#{Thread.list.size} threads"
threads.each do |t|
  t.join
end