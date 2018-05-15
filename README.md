# Python-status-check

- collect info about current Instance;
- collect info about remoute Instance;
- check connection via ports 22 & 80;
- if connection closed:
  - compare current IP with Elastic
  - if current IP is not elastic -> reassign elastic Ip to current instance
  - stop "disabled/blocked" instance
  - disable cron job
