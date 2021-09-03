// Hover effect on add to cart buttons for product details page.
document.getElementById("add-to-cart").onmouseover = function() {mouseOver()};
document.getElementById("add-to-cart").onmouseout = function() {mouseOut()};
let add = '+'
let left = 'Add to Cart'


function mouseOver() {
    document.getElementById('add-to-cart').setAttribute('value', add);
    
  }

function mouseOut() {
    document.getElementById('add-to-cart').setAttribute('value', left);
  }


