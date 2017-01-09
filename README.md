# ansible-nginx-swagger-example
A test to generate valid nginx syntax from a swagger.yml file.

## Usage
`ansible-playbook swagger_to_nginx.yml -e "swaggerfile=/path/to/swagger.yaml"`

This will create `/tmp/swagger.out`, which should be a valid nginx server block.

## Why?
The swagger yaml spec is nice in that it (should be) valid yaml.
Ansible loves yaml!  As a matter of fact, you can slurp up a yaml file with [include_vars](http://docs.ansible.com/ansible/include_vars_module.html).

Also, for Swagger, the only required thing beyond "swagger","info" is also ["paths"](http://swagger.io/specification/#fixed-fields-15).

Paths are also expected, thus leading to the thought 'this can produce valid webserver output,' and it can!

I like Nginx and CI/CD, so I made this.  I would imagine httpd, lighttpd, and anything else would be just as simple to produce something for.
