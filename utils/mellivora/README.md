This is a messy list of what I changed on mellivora to make it suit my own purposes.

## Changes

### `Dockerfile`
Add `libonig-dev` to `apt install` list, to fix a bug
Add `RUN ln -snf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && dpkg-reconfigure -f noninteractive tzdata` at the start, to set timezone

### `htdocs/actions/reset_password.php`
Comment pretty much the entire thing out, and adding `message_generic("Failure", "Password reset is disabled. Contact Kevin if you cannot login to your account.");`. Don't want people abusing the password reset stuff, and we're doing it on a small enough scale to deal with password resets manually. 

### `htdocs/home.php`
Comment out entire thing displaying news, and adding this block:
```php
if (cache_start(CONST_CACHE_NAME_HOME, Config::get('MELLIVORA_CONFIG_CACHE_TIME_HOME'))) {

    $news = db_query_fetch_all('SELECT * FROM news ORDER BY added DESC');
    foreach ($news as $item) {
        echo '<link rel="stylesheet" href="https://stackedit.io/style.css">
        <div class="news-container">';
            section_head($item['title']);
            echo '
            <div class="news-body">
                ',$item['body'],'
            </div>
        </div>
        ';
    }

    cache_end(CONST_CACHE_NAME_HOME);
}
```
I'm writing the syllabus in markdown, then exporting as HTML. The original code uses bbcode, which is less versatile.

### `htdocs/register.php`
Replace `Registration is currently closed, but you can still <a href="interest">register your interest for upcoming events</a>.` to `Registration is currently closed. Please check back later.`. No need for interest registration stuff.

### `htdocs/reset_password.php
Comment everything out, adding:
```php
head(lang_get('reset_password'));
message_inline_blue('Password reset is disabled. Contact Kevin if you cannot login to your account.');
foot();
```
Again, this is to disable password resets. This is the front facing page, while the one we did earlier is the api to process the request. Both are gone.

### `include/layout/forms.inc.php`
Removed `<option disabled selected>-- ',lang_get('please_select_country'),' --</option>`. We just don't have a use for selecting countries.

### `include/session.inc.php`
Commented out `send_email(array($email), $email_subject, $email_body);`. No need to send emails.

### `htdocs/challenges.php`
Changed line 236 to be `',$challenge['description'],'`, just because I don't like bbcode. Don't have time to grab a markdown parser in PHP, so I'm doing it by hand and putting the HTML in the description. I know this means potential for XSS but I'm in full control of the description and no one else is.

### `include/layout/scores.inc.php` and `include/layout/user.inc.php
Documented [here](https://github.com/Nakiami/mellivora/pull/128)

## Additions

### `include/config/config.inc.php` and `include/config/db.inc.php`
Configurations. Nuff said.

### `docker-compose.yml`
Custom docker configuration, not really that custom but still worth hiding since it contains some database creds.
