## Q1-Explain all the CSS positions(static, fixed, sticky, relative, absolute) with one code example each.

1.Static:

Static positioning is the default behavior for elements.
Elements with position: static are positioned according to the normal flow of the document.
They are not affected by the top, bottom, left, or right properties.
Example:

html
```

<div class="static-position">
  This is a static position example.
</div>

css

.static-position {
  position: static;
}
```

2.Fixed:

Elements with position: fixed are positioned relative to the viewport.
They are removed from the normal flow of the document.
Fixed elements stay in a fixed position even when the page is scrolled.
Example:

html
```
<div class="fixed-position">
  This is a fixed position example.
</div>

css

.fixed-position {
  position: fixed;
  top: 20px;
  right: 20px;
}
```
3.Sticky:

Elements with position: sticky are positioned based on the user's scroll position.
They are initially positioned according to the normal flow of the document but become fixed once they reach a specified scroll position.
Example:

html
```
<div class="sticky-position">
  This is a sticky position example.
</div>

css

.sticky-position {
  position: sticky;
  top: 20px;
}
```

4.Relative:

Elements with position: relative are positioned relative to their normal position.
They can be moved from their original position using the top, bottom, left, or right properties.
Example:

html
```
<div class="relative-position">
  This is a relative position example.
</div>

css

.relative-position {
  position: relative;
  left: 20px;
}
```

5.Absolute:

Elements with position: absolute are positioned relative to their closest positioned ancestor (parent or ancestor with a position other than static).
If no positioned ancestor is found, the element will be positioned relative to the initial containing block.
Example: 
html
```
<div class="absolute-position">
  This is an absolute position example.
  <div class="inner-position">
    This is an inner element with absolute position.
  </div>
</div>

css

.absolute-position {
  position: relative;
}
.inner-position {
  position: absolute;
  top: 20px;
  right: 20px;
}
```
