module.exports = function(grunt) {

    var mozjpeg = require('imagemin-mozjpeg');

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        'min': {
            'dist': {
                'src': ['_js/jquery/*.js','_js/*.js'],
                'dest': '../assets/scripts.min.js'
            }
        },
        'cssmin': {
            'dist': {
                'src': ['_css/*.css'],
                'dest': '../assets/styles.min.css'
            }
        },
        'imagemin': {
            options: {
                optimizationLevel: 7,
                svgoPlugins: [{ removeViewBox: false }],
                use: [mozjpeg()]
              },
            dynamic: {
                files: [{
                    expand: true,
                    cwd: '_imgs/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: '../assets/images/'
                }]
            }
        },
        htmlmin: {                                     // Task
            dist: {                                      // Target
              options: {                                 // Target options
                removeComments: true,
                collapseWhitespace: true
              },
              files: {                                   // Dictionary of files
                  '../templates/tcsite/index.html': '_html/tcsite/index.html',     // 'destination': 'source'
                  '../templates/tcsite/carousel.html': '_html/tcsite/carousel.html',
                  '../templates/tcsite/top_img.html': '_html/tcsite/top_img.html',
                  '../templates/tcsite/footer.html': '_html/tcsite/footer.html',
                  '../about/templates/about/about.html': '_html/about.html',
                  '../games/templates/games/games.html': '_html/games.html',
                  '../games/templates/games/game.html': '_html/game.html',
                  '../blog/templates/blog/blog.html': '_html/blog.html',
                  '../contacts/templates/contacts/contacts.html': '_html/contacts.html',
                  '../homepage/templates/homepage/home.html': '_html/home.html',
              }
            }
        },
        'watch': {
            scripts: {
                files: ['_js/*.js','js/jquery/*.js'],
                tasks: ['min'],
                options: {
                    spawn: false,
                },
            },
            css: {
                files: ['_css/*.css'],
                tasks: ['cssmin'],
                options: {
                    spawn: false,
                },
            },
            html: {
                files: ['_html/*.html', '_html/tcsite/*.html'],
                tasks: ['htmlmin'],
                options: {
                    spawn: false,
                },
            },
            img: {
                files: ['_imgs/**/*.{png,jpg,gif}'],
                tasks: ['imagemin'],
                options: {
                    spawn: false,
                },
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-yui-compressor');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-htmlmin');

    grunt.registerTask('default', ['min', 'cssmin', 'imagemin', 'htmlmin']);
};