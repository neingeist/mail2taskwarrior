Add a task to [taskwarrior](http://taskwarrior.org) via email. Makes use of the
[taskw](https://github.com/ralphbean/taskw) Python bindings.


For use with procmail or maildrop. Example using maildrop's `.mailfilter`:

~~~
if ($SIZE < 8192 && /^From:.*myaddress@example.com/ && /^To:.*taskwarrior@/)
{
  log "add task via mail2taskwarrior"
  xfilter "devel/mail2taskwarrior/mail2taskwarrior"
  exit
}
~~~
