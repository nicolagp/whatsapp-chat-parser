# whatsapp-chat-parser
Module to parse a whatsapp chat txt file into csv. A few things to notice
are that currently the module can only deal with the following formatting:

`[7/16/18, 10:26:28 AM] message author: message text`

## Usage
Create a parser class where you specify the name of the file that must be in
the same directory:

`parser = WppParser('file.txt')`

Then you can use the to_csv method to generate a csv file with the contents
 of your chat file and the desired name.
 
 `parser.to_csv('filename.csv')`