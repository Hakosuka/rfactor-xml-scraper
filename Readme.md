I began this project as a way to learn a new programming language. As a fan of the 
racing game rFactor, I came up with a "career mode" of sorts using F1 mods for 
different seasons. To add a bit of realism, in the event of a severe crash (let's 
say, at the first corner of Monaco), I'd stop and then restart the race.

Each layout of every track in rFactor has at least one associated event (e.g. 
Monaco could have the 2015 and 2016 Monaco Grands Prix on the full track, and the 
2015 Monaco ePrix on the Formula E track), which in turn corresponds to a .gdb file.
Within that file, you could store a default grid lineup.

The results of every kind of session - testing, practice, qualifying or the race - 
are stored in .xml files. Every driver's position in a session is stored within 
<Position> tags, and their name is stored within <Name> tags. Rather than take a 
few minutes to create a new grid lineup manually by editing the track's .gdb file
in a text editor, I wanted instead to write a web scraper program which would 
import results from the .xml file and export them to the .gdb fiel that I wanted.

TODO:
1. Implement importing of .xml documents.
2. Implement scraping of said .xml document for necessary data.
3. Export that data to a plaintext document (I can easily just copy and paste the
grid lineup from there anyway).
4. Export that data to the correct place in the relevant .gdb document.
