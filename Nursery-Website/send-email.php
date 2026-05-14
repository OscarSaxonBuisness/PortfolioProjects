<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $fullname = htmlspecialchars($_POST['fullname']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    $to = "oscarsaxon951@gmail.com"; // change if needed
    $subject = "Nursery Visit Request";

    $body = "New visit enquiry from website:\n\n";
    $body .= "Full Name: $fullname\n";
    $body .= "Email: $email\n\n";
    $body .= "Message:\n$message";

    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "<h2 style='font-family:Montserrat;'>Thank you! Your message has been sent.</h2>";
    } else {
        echo "<h2 style='font-family:Montserrat;'>Sorry, something went wrong. Please try again.</h2>";
    }
}
?>
