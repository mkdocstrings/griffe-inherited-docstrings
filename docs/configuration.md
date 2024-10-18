## `merge`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**


- `merge=False`: This setting allows the docstring of the parent method to be inherited if the subclass method does not provide its own docstring. It ensures that a method without documentation in a subclass still displays useful inherited information from its parent.
- `merge=True`: This setting merges the docstrings from parent methods, concatenating all parent classes' docstrings with any additional text provided by the subclass. This is useful for methods where the subclass adds supplementary notes or overrides part of the behavior but still shares the general purpose of the parent method. Docstrings are concatenated with a blank line between them to let mkdocs render a separate paragraph for each docstring.

/// admonition | Preview
    type: preview

//// tab | merge = False
```python
class Shape:
    contour: list[Point]
    def surface_area(self):
        """Return the surface area in square meters."""
        return numerical_integration(self.contour)

class Rectange(Shape)
    def surface_area(self):
        return distance(self.cotour[2], self.contour[0]) * distance(self.contour[3], self.contour[1])
```

Should output a documentation like this:
```
Shape
    surface_area
        Return the surface area in square meters.
    ...

Rectangle
    surface_area
        Return the surface area in square meters.
    ...
```
////

//// tab | merge = True
```python
class Shape:
    contour: list[Point]
    def surface_area(self):
        """Return the surface area in square meters."""
        return numerical_integration(self.contour)

class Rectange(Shape)
    def surface_area(self):
		"""Note: This is way faster than the calculation for general shapes!"""
        return distance(self.cotour[2], self.contour[0]) * distance(self.contour[3], self.contour[1])
```

Should output a documentation like this:
```
Shape
    surface_area
        Return the surface area in square meters.
    ...

Rectangle
    surface_area
        Return the surface area in square meters.

        Note: This is way faster than the calculation for general shapes!
    ...
```
////

///
