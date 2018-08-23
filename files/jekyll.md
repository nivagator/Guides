# Jekyll Notes

## Installing Jekyll on Linux
[Before you start, make sure your system has the following:](https://jekyllrb.com/docs/installation/#requirements) (As of 2018-05-01)

- Ruby version 2.2.5 or above, including all development headers (ruby installation can be checked by running `ruby -v`)
- RubyGems (which you can check by running `gem -v`)
- GCC and Make (in case your system doesn’t have them installed, which you can check by running `gcc -v`,`g++ -v` and `make -v` in your system’s command line interface)

#### Steps
1. `sudo apt-get install ruby ruby-dev build-essential`
2. ```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME=$HOME/gems' >> ~/.bashrc
echo 'export PATH=$HOME/gems/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```
3. `gem install jekyll bundler`



## Starting a new Jekyll project
From within your Jekyll project folder, run `jekyll new project-name`

## Troubleshooting
2018-05-01 - `cannot load such file` error - https://github.com/rubygems/rubygems/issues/2180
  - `sudo gem update --system 2.7.4`
  - `gem uninstall bundler`
  - `sudo gem install bundler --version '1.16.0'`

## Links
[Jekyll & Liquid Cheatsheet](https://gist.github.com/smutnyleszek/9803727)
[Make a Static Website with Jekyll](https://www.taniarascia.com/make-a-static-website-with-jekyll/)
