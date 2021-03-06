var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var htmlmin = require('gulp-htmlmin');
var uncss = require('gulp-uncss');
var watch = require('gulp-watch');

gulp.task('minify-css', function() {
    return gulp.src('css/*.css')
        .pipe(concat('styles.min.css'))
        .pipe(cleanCSS({keepSpecialComments: '0'}))
        //.pipe(uncss({ html: ['html/**/*.html', 'js/*.*']}))
        .pipe(gulp.dest('../assets'));
});

gulp.task('minify-js', function() {
    return gulp.src('js/*.js')
        .pipe(concat('scripts.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('../assets'));
});

gulp.task('minify-html', function() {
    gulp.src('html/about.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../about/templates/about'))

    gulp.src('html/contacts.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../contacts/templates/contacts'))

    gulp.src('html/work.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../works/templates/works'))

    gulp.src('html/works.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true, ignoreCustomFragments: [/==/]}))
    .pipe(gulp.dest('../works/templates/works'))

    gulp.src('html/home.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../homepage/templates/homepage'))

    gulp.src('html/post.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../blog/templates/blog'))

    gulp.src('html/posts.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../blog/templates/blog'))

    gulp.src('html/tcsite/carousel.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../templates/tcsite'))

    gulp.src('html/tcsite/footer.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../templates/tcsite'))

    gulp.src('html/tcsite/index.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../templates/tcsite'))

    gulp.src('html/tcsite/top_img.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../templates/tcsite'))

    gulp.src('html/tcsite/top_img_full.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../templates/tcsite'))

    gulp.src('html/tcsite/top_video.html')
    .pipe(htmlmin({collapseWhitespace: true, removeComments: true}))
    .pipe(gulp.dest('../templates/tcsite'))
});

gulp.task('default', function() {
    gulp.watch('html/**', function(event) {
        gulp.run('minify-html');
    });

    gulp.watch('css/**', function(event) {
        gulp.run('minify-css');
    });

    gulp.watch('js/**', function(event) {
        gulp.run('minify-js');
    });
});