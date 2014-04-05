#!/usr/bin/ruby

require 'thread'

mutex = Mutex.new
maximo = -1
threads = []
th=0

arr = (0..100000).to_a.sample(1000)

j=0

puts "Arreglo:"
p arr

for i in 1..arr.size/50 do
  threads << Thread.new(j,i) do |k,l|
    mutex.synchronize do
      puts "Max= #{ arr[k,50].max} entre #{k},#{k+50}"
      if  maximo < arr[k,50].max
        maximo = arr[k,50].max
         th=l
      end
    end
  end
  j+=50
end

threads.each(&:join)

puts "Max: #{maximo}  encontrado por Threads: #{th}"