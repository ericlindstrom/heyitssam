<?php
    $page = new stdClass;
    $page->title = '404';
    $page->body_class = 'index error';
    include "includes/header.php";
?>
    <section>
    <h1>Oops! The page you were looking for could not be found.</h1>
    <h1>Why not come on back to the <a href="/">Homepage</a></h1>
    </section>

<?php include "includes/footer.php"; ?>
