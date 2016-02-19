#Lab4#

We (table 7) found bugs in FreeBSD documentation:

#Bug 1#
[https://www.freebsd.org/doc/en_US.ISO8859-1/books/porters-handbook/slow-sources.html](https://www.freebsd.org/doc/en_US.ISO8859-1/books/porters-handbook/slow-sources.html)

This is the .diff:

"-    <para>If the port requires some additional `patches' that are"

"+    <para>If the port requires some additional 'patches' that are"

[the difference here is the single quote fix instead of apostrophe]

[Bug report link here](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207340)


#Bug 2#

very similar to bug 1
[Bug report link here](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207345)


#Bug 3 (my bug)#
[https://www.freebsd.org/doc/en_US.ISO8859-1/books/porters-handbook/rc-scripts.html](https://www.freebsd.org/doc/en_US.ISO8859-1/books/porters-handbook/rc-scripts.html)
[XML location](https://svnweb.freebsd.org/doc/head/en_US.ISO8859-1/books/porters-handbook/special/chapter.xml?view=markup)

This is the .diff:

--- chapter.xml (revision 48199)
+++ chapter.xml (working copy)
@@ -5396,7 +5396,7 @@
        <step>
          <para>Make sure there is no
            <literal>KEYWORD: &os;</literal> present.  This has

"-           not been necessary or desirable for years.  It is also"

"+           not been necessary nor desirable for years.  It is also
            an indication that the new script was copy/pasted from
            an old script, so extra caution must be given to the
            review.</para>"


[Bug report link here](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207353)
