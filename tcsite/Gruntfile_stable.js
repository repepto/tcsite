module.exports = function(grunt) {

    var mozjpeg = require('imagemin-mozjpeg');

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        'min': {
            'dist': {
                'src': ['_js/jquery/*.js','_js/*.js'],
                'dest': 'assets/scripts.min.js'
            }
        },
        'cssmin': {
            'dist': {
                'src': ['_css/*.css'],
                'dest': 'assets/styles.min.css'
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
                    dest: 'assets/images/'
                }]
            }
        }
    });

    grunt.loadNpmTasks('grunt-yui-compressor');
    grunt.loadNpmTasks('grunt-contrib-imagemin');

    grunt.registerTask('default', ['min', 'cssmin', 'imagemin']);
};