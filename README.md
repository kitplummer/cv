Kit Plummer's CV
==

See it here: [http://kitplummer.github.io/cv](http://kitplummer.github.io/cv)

Build with: [https://github.com/there4/markdown-resume](https://github.com/there4/markdown-resume)

See the `Makefile` for details on building.

Or run stuff directly.

```
$ md2resume html -t readable kp-resume.md .
$ md2resume pdf -t readable kp-resume.md .
```

With Docker:

```
docker run -v ${PWD}:/. there4/markdown-resume md2resume html -t readable kp-resume.md .
```
