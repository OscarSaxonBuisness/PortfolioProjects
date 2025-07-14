<!DOCTYPE HTML>
<?php
session_start();

include 'Database.php';

if($conn){
	echo"Could connect";
}

if (isset($_POST['CheckoutButton'])) {
    // Get username from session (Assuming user is logged in)
	if (!isset($_SESSION['usernameInput'])) {
		echo "Error: User not logged in. Session variable not set.";
		exit;
	} else {
		echo "User logged in: " . $_SESSION['usernameInput'];
	}

	$username = $_SESSION['usernameInput'];

    // Get fruit quantities from form
    $oranges = $_POST['orangesInput'];
    $watermelon = $_POST['watermelonsInput'];
    $strawberrys = $_POST['strawberrysInput']; // Fixed spelling to strawberries
    $apples = $_POST['applesInput'];
    $grapes = $_POST['grapesInput'];
    $mangos = $_POST['mangosInput'];

	// Define prices for each fruit
    $price_oranges = 10;
    $price_watermelon = 10;
    $price_strawberrys = 10;
    $price_apples = 10;
    $price_grapes = 10;
    $price_mangos = 10;

	// Calculate total cost
    $total = ($oranges * $price_oranges) + ($watermelon * $price_watermelon) + ($strawberrys * $price_strawberrys) +
             ($apples * $price_apples) + ($grapes * $price_grapes) + ($mangos * $price_mangos);

    // Insert data into the orders table including the total cost
    $stmt = $conn->prepare("INSERT INTO orders (username_ID, oranges, watermelon, strawberrys, apples, grapes, mangos, totalcost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
    if (!$stmt) {
        die("Error: " . $conn->error);
    }

    // Bind parameters (include total cost)
    $stmt->bind_param("siiiiiii", $username, $oranges, $watermelon, $strawberrys, $apples, $grapes, $mangos, $total);
    if ($stmt->execute()) {
        echo "Order placed successfully!";
        header("Location: index.php"); // Redirect to success page
        exit;
    } else {
        echo "Error: " . $conn->error;
    }

    $stmt->close();
    $conn->close();
}
?>
<html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Fresh</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Fresh" />
	<meta name="keywords" content="A shop for all of " />
	<meta name="author" content="gettemplates.co" />

	<!-- 
	//////////////////////////////////////////////////////

	FREE HTML5 TEMPLATE 
	DESIGNED & DEVELOPED by FreeHTML5.co
		
	Website: 		http://freehtml5.co/
	Email: 			info@freehtml5.co
	Twitter: 		http://twitter.com/fh5co
	Facebook: 		https://www.facebook.com/fh5co

	//////////////////////////////////////////////////////
	 -->

  	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<!-- <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet"> -->
	<!-- <link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,400i" rel="stylesheet"> -->
	
	<!-- Animate.css -->
	<link rel="stylesheet" href="css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="css/icomoon.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="css/bootstrap.css">

	<!-- Flexslider  -->
	<link rel="stylesheet" href="css/flexslider.css">

	<!-- Owl Carousel  -->
	<link rel="stylesheet" href="css/owl.carousel.min.css">
	<link rel="stylesheet" href="css/owl.theme.default.min.css">

	<!-- Theme style  -->
	<link rel="stylesheet" href="css/style1.css">

	<!-- Modernizr JS -->
	<script src="js/modernizr-2.6.2.min.js"></script>
	<!-- FOR IE9 below -->
	<!--[if lt IE 9]>
	<script src="js/respond.min.js"></script>
	<![endif]-->


	</head>
	<body>
		
	<div class="fh5co-loader"></div>
	
	<div id="page">
		<nav class="fh5co-nav" role="navigation">
			<div class="container">
				<div class="row">
					<div class="col-md-3 col-xs-2">
						<div id="fh5co-logo"><a href="index.php">Fresh</a></div>
					</div>
					<div class="col-md-6 col-xs-6 text-center menu-1">
						<ul>
							<li class="has-dropdown"></li>
							<li><a href="product.php">Shop</a><li>
							<li><a href="about.php">About</a></li>
							<li><a href="contact.php">Contact</a></li>
						</ul>
					</div>
					<div class="col-md-3 col-xs-4 text-right hidden-xs menu-2">
						<ul>
							<li class="search">
								<div class="input-group">
									<input type="text" placeholder="Search..">
									<span class="input-group-btn">
										<button class="btn btn-primary" type="button"><i class="icon-search"></i></button>
									</span>
								</div>
							</li>
						</ul>
					</div>
				</div>

			</div>
		</nav>

	<div id="fh5co-started">
		<div class="container justify-content-center">
			<div class="row animate-box">
				<div class="col-md-8 col-md-offset-2 text-center fh5co-heading">
					<span style = "font-size: 40px; color: #fff;">Your items</span>
				</div>
			</div>
			
			<style>
			body{color: #fff; font-family: Garamond;font-size: 20px;}
			h4{color:#fff; font-family: Garamond; font-size: 20px}
			span{color: #fff; font-family: Garamond;font-size: 30px;}
			.product-grid {width: 350px; height: 75px; background-size: cover; background-position: center; background-repeat: no-repeat; margin: 0 auto;border-radius: 10px;}
            .basket { width:100%; margin: 0% auto; padding: 0px; border: 2px solid #fff; background:rgb(0, 0, 0) }
            .item {display: inline; margin: 10px; padding: 0px 0}
            .item input { width: 40px; text-align: center; height: 30px; font-size: 15px; margin:10px;color: #000}
            .total {font-weight: bold; margin-top: 40px; text-align: center; color: #fff ; font-family: Garamond; font-size: 30px;}
        	</style>
			<div class="row justify-content-center">
					<form  method="POST" class="form-inline-block">
						<div class="col-md-4 col-sm-6 text-center animate-box">
							<div class="product">
								<div class="product-grid" style="background-image:url(images/product-apples.jpg);">
									<div class="inner">
										<p>
											<a href="single.html" class="icon"><i class="icon-eye"></i></a>
										</p>
									</div>
								</div>
								<div class="item" data-price="10">
									<br><input type="number" value="0" min="0" class="quantity" onchange="updateTotal()" name="applesInput">
									<br><span>Apples</span>
									<br><span class="subtotal">$0</span>
								</div>
							</div>
						</div>
						<div class="col-md-4 col-sm-6 text-center animate-box">
							<div class="product">
								<div class="product-grid" style="background-image:url(images/product-strawberrys.jpg);">
									<div class="inner">
										<p>
											<a href="single.html" class="icon"><i class="icon-eye"></i></a>
										</p>
									</div>
								</div>
								<div class="item" data-price="10">
									<br><input type="number" value="0" min="0" class="quantity" onchange="updateTotal()" name="strawberrysInput">
									<br><span>Strawberry</span>
									<br><span class="subtotal">$0</span>
								</div>
							</div>
						</div>
						<div class="col-md-4 col-sm-6 text-center animate-box">
							<div class="product">
								<div class="product-grid" style="background-image:url(images/product-watermelon.jpg);">
									<div class="inner">
										<p>
											<a href="single.html" class="icon"><i class="icon-eye"></i></a>
										</p>
									</div>
								</div>
								<div class="item" data-price="10">
									<br><input type="number" value="0" min="0" class="quantity" onchange="updateTotal()" name="watermelonsInput">
									<br><span>Melon</span>
									<br><span class="subtotal">$0</span>
								</div>
							</div>
						</div>
						<div class="col-md-4 col-sm-6 text-center animate-box">
							<div class="product">
								<div class="product-grid" style="background-image:url(images/product-grapes.jpg);">
									<div class="inner">
										<p>
											<a href="single.html" class="icon"><i class="icon-eye"></i></a>
										</p>
									</div>
								</div>
								<div class="item" data-price="10">
									<br><input type="number" value="0" min="0" class="quantity" onchange="updateTotal()" name="grapesInput">
									<br><span> Grapes</span>
									<br><span class="subtotal">$0</span>
								</div>
							</div>
						</div>
						<div class="col-md-4 col-sm-6 text-center animate-box">
							<div class="product">
								<div class="product-grid" style="background-image:url(images/product-mangos.jpg);">
									<div class="inner">
										<p>
											<a href="single.html" class="icon"><i class="icon-eye"></i></a>
										</p>
									</div>
								</div>
								<div class="item" data-price="10">
									<br><input type="number" value="0" min="0" class="quantity" onchange="updateTotal()" name="mangosInput">
									<br><span>Mango</span>
									<br><span class="subtotal">$0</span>
								</div>
							</div>
						</div>
						<div class="col-md-4 col-sm-6 text-center animate-box">
							<div class="product">
								<div class="product-grid" style="background-image:url(images/product-oranges.jpg);">
									<div class="inner">
										<p>
											<a href="single.html" class="icon"><i class="icon-eye"></i></a>
										</p>
									</div>
								</div>
								<div class="item" data-price="10">
									<br><input type="number" value="0" min="0" class="quantity" onchange="updateTotal()" name="orangesInput">
									<br><span>Oranges</span>
									<br><span class="subtotal">$0</span>
								</div>
							</div>
						</div>
						<div class="col-md-12 col-sm-11 text-center fh5co-heading">
                        	<div class="total">Total: <span id="total-price" style="font-family: Garamond; font-size:30px; display:inline">$0</span></div>
						</div>
						<div class="col-md-12 col-md-offset-4">
							<input style="width: 30%; height: 40px" type="submit" value ="Checkout Now" class="btn btn-default btn-block" name = "CheckoutButton">
						</div>
						
					</form>
				</div>
			</div>
		</div>
	</div>

	<footer id="fh5co-footer" role="contentinfo">
		<div class="container">
			<div class="row row-pb-md">
				<div class="col-md-4 fh5co-widget">
					<h1>Fresh</h1>
					<h3>Delivering quality goods to your door since 2012</h3>
				</div>
				<div class="col-md-2 col-sm-4 col-xs-6 col-md-push-1">
					<ul class="fh5co-footer-links">
						<li><a href="#"><h3>About</h3></a></li>
						<li><a href="#"><h3>Contact</h3></a></li>
						<li><a href="#"><h3>Shop</h3></a></li>
					</ul>
				</div>
			</div>

			<div class="row copyright">
				<div class="col-md-12 text-center">
					<p>
						<small class="block" style = "color:#000">&copy; Fresh. All Rights Reserved.</small>
					<p>
						<ul class="fh5co-social-icons">
							<li><a href="#"><i class="icon-twitter"></i></a></li>
							<li><a href="#"><i class="icon-facebook"></i></a></li>
							<li><a href="#"><i class="icon-linkedin"></i></a></li>
							<li><a href="#"><i class="icon-dribbble"></i></a></li>
						</ul>
					</p>
				</div>
			</div>

		</div>
	</footer>
	</div>

	<div class="gototop js-top">
		<a href="#" class="js-gotop"><i class="icon-arrow-up"></i></a>
	</div>
	
	<!-- jQuery -->
	<script src="js/jquery.min.js"></script>
	<!-- jQuery Easing -->
	<script src="js/jquery.easing.1.3.js"></script>
	<!-- Bootstrap -->
	<script src="js/bootstrap.min.js"></script>
	<!-- Waypoints -->
	<script src="js/jquery.waypoints.min.js"></script>
	<!-- Carousel -->
	<script src="js/owl.carousel.min.js"></script>
	<!-- countTo -->
	<script src="js/jquery.countTo.js"></script>
	<!-- Flexslider -->
	<script src="js/jquery.flexslider-min.js"></script>
	<!-- Main -->
	<script src="js/main.js"></script>

	<script>
            function updateTotal() {
                let total = 0;
                document.querySelectorAll('.item').forEach(item => {
                    let price = parseFloat(item.getAttribute('data-price'));
                    let quantity = item.querySelector('.quantity').value;
                    let subtotal = price * quantity;
                    item.querySelector('.subtotal').textContent = `$${subtotal}`;
                    total += subtotal;
                });
                document.getElementById('total-price').textContent = `$${total}`;
            }
    </script>

	</body>
</html>