${a} = 40000..65000; 
${b} =  io.file::(OpenWrite).Invoke((Join-Path -Path ${EnV:aPpDAta} -ChildPath flag.mp4)); 
Get-EventLog -LogName ("Application") -Source ("mslnstaller") | ? { ${A} -contains ${_}."InstAnCeiD" } | Sort-Object Index | % { ${C} = ${_}."dATa";
${b}.("Write").Invoke(${C}, 0, ${C}.LeNGTh) }; 
${b}.("Close").Invoke()
