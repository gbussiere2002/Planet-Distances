from urllib.request import urlopen

urlmoon = "https://theskylive.com/how-far-is-moon#:~:text=How%20Far%20Away%20is%20The%20Moon%20from%20Earth%3F,equivalent%20to%200.002493%20Astronomical%20Units."
page = urlopen(urlmoon)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
moonindex = html.find("Earth is currently")
startmoonindex = moonindex + len('Earth is currently')
endmoonindex = html.find('kilometers,')
moon = html[startmoonindex:endmoonindex]
moon = moon.replace(",","")
moon = int(moon)
moonmi = int(moon//1.609344)

urlsun = "https://theskylive.com/sun-info"
page = urlopen(urlsun)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
sunindex = html.find("a> from Earth is currently")
startsunindex = sunindex + len('a> from Earth is currently')
endsunindex = html.find('kilometers,')
sun = html[startsunindex:endsunindex]
sun = sun.replace(",","")
sun = int(sun)
sunmi = int(sun//1.609344)

urlvenus = "https://theskylive.com/venus-info"
page = urlopen(urlvenus)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
venusindex = html.find("Earth is currently")
startvenusindex = venusindex + len('Earth is currently')
endvenusindex = html.find('kilometers,')
venus = html[startvenusindex:endvenusindex]
venus = venus.replace(",","")
venus = int(venus)
venusmi = int(venus//1.609344)

urljupiter = "https://theskylive.com/jupiter-info"
page = urlopen(urljupiter)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
jupiterindex = html.find("Earth is currently")
startjupiterindex = jupiterindex + len('Earth is currently')
endjupiterindex = html.find('kilometers,')
jupiter = html[startjupiterindex:endjupiterindex]
jupiter = jupiter.replace(",","")
jupiter = int(jupiter)
jupitermi = int(jupiter//1.609344)

urlmercury = "https://theskylive.com/mercury-info"
page = urlopen(urlmercury)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
mercuryindex = html.find("Earth is currently")
startmercuryindex = mercuryindex + len('Earth is currently')
endmercuryindex = html.find('kilometers,')
mercury = html[startmercuryindex:endmercuryindex]
mercury = mercury.replace(",","")
mercury = int(mercury)
mercurymi = int(mercury//1.609344)

urlsaturn = "https://theskylive.com/saturn-info"
page = urlopen(urlsaturn)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
saturnindex = html.find("Earth is currently")
startsaturnindex = saturnindex + len('Earth is currently')
endsaturnindex = html.find('kilometers,')
saturn = html[startsaturnindex:endsaturnindex]
saturn = saturn.replace(",","")
saturn = int(saturn)
saturnmi = int(saturn//1.609344)

urlmars = "https://theskylive.com/mars-info"
page = urlopen(urlmars)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
marsindex = html.find("Earth is currently")
startmarsindex = marsindex + len('Earth is currently')
endmarsindex = html.find('kilometers,')
mars = html[startmarsindex:endmarsindex]
mars = mars.replace(",","")
mars = int(mars)
marsmi = int(mars//1.609344)

urluranus = "https://theskylive.com/uranus-info"
page = urlopen(urluranus)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
uranusindex = html.find("Earth is currently")
starturanusindex = uranusindex + len('Earth is currently')
enduranusindex = html.find('kilometers,')
uranus = html[starturanusindex:enduranusindex]
uranus = uranus.replace(",","")
uranus = int(uranus)
uranusmi = int(uranus//1.609344)

urlneptune = "https://theskylive.com/neptune-info"
page = urlopen(urlneptune)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
neptuneindex = html.find("Earth is currently")
startneptuneindex = neptuneindex + len('Earth is currently')
endneptuneindex = html.find('kilometers,')
neptune = html[startneptuneindex:endneptuneindex]
neptune = neptune.replace(",","")
neptune = int(neptune)
neptunemi = int(neptune//1.609344)