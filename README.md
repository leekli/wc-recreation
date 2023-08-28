# ccwc - [coding challenge] word count

## 🧐 About Repo

### In this repo, I build my own version of the Unix command line tool: `wc`

I have called it `ccwc` - coding challenge word count.

Part of this Coding challenge: https://codingchallenges.fyi/challenges/challenge-wc

**Written in:** Python 🐍

## 👨‍🏫 Set-up

1. Clone the repo:

   ```terminal
   $ git clone https://github.com/leekli/wc-recreation.git
   ```

2. Ensure at least Python 3.10 is installed.

3. A test file `art_of_war.txt` is supplied to use as an example.

## 💻 Commands & Options available

- **Help:** Shows the help message, explanation of the application, and options available.

  ```terminal
  $ ./ccwc.py -h
  ```

> [!NOTE]
> All commands below can be used either by giving a file name, or piping through standard input (stdin).

- **-c [file_name | stdin]:** Displays the number of bytes in the input file / standard input given

  - With a file name:

  ```terminal
  $ ./ccwc.py -c art_of_war.txt
  ```

  - With standard input:

  ```terminal
  $ cat art_of_war.txt | ./ccwc.py -c

  ```

<br></br>

- **-l [file_name | stdin]:** Displays the number of lines in the input file / standard input given

  - With a file name:

  ```terminal
  $ ./ccwc.py -l art_of_war.txt
  ```

  - With standard input:

  ```terminal
  $ cat art_of_war.txt | ./ccwc.py -l

  ```

  <br></br>

- **-w [file_name | stdin]:** Displays the number of words in the input file / standard input given

  - With a file name:

  ```terminal
  $ ./ccwc.py -w art_of_war.txt
  ```

  - With standard input:

  ```terminal
  $ cat art_of_war.txt | ./ccwc.py -w

  ```

  <br></br>

- **-m [file_name | stdin]:** Displays the number of characters in the input file / standard input given

  - With a file name:

  ```terminal
  $ ./ccwc.py -m art_of_war.txt
  ```

  - With standard input:

  ```terminal
  $ cat art_of_war.txt | ./ccwc.py -m

  ```

<br></br>

> [!NOTE]
> The following command below can only currently be used either by giving a file name.

- **[file_name]:** No flags given, only a file name. Displays the number of lines, bytes and characters in the input file given.

  - With a file name:

  ```terminal
  $ ./ccwc.py art_of_war.txt
  ```
