# KalkSpace Infra

Frickel Config Management via Ansible

Ask high-level questions in the [forums](https://discuss.kalk.space/c/infrastruktur/digital-infra/18) or in [`#infrastruktur`](https://app.slack.com/client/TP5CDET5E/CQ79KQ1JN).
For specific problems or enhancements, please open an issue.

## Metrics

This manages metrics services living at https://metrics.kalk.space. See the [role readme](./roles/metrics/README.md) for details.

## Getting started

The config management is based on [Ansible](https://docs.ansible.com/ansible/latest/index.html). To be able to test and apply changes to this repo you need to install it.

Configuration is split into roles:
- `roles/metrics` - Configures [metrics gathering & display services](#metrics)

### Testing changes

Use this command to test changes before rolling them to a live node (requires Docker):

```sh
ansible-playbook test.yml --diff
```

This will not attempt to bring up any containers. It only tests config generation.

To check the config files, look at the diff output or run `docker exec -ti <container_id> bash`.

If you want to start a subsequent run with a fresh test environment, run:

```sh
ansible-playbook test.yml --diff -e recreate_test_env=true
```

### Access to secrets

Secrets are encrypted via [Ansible vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html). This allows us to not commit them in plaintext and still enjoy all benefits of git.

All secrets should be stored in `vault/secrets.yml` to collect them in a single place. `vault/test-dummies.yml` is used for setting mock values for testing.

The vault needs a password to decrypt secrets for production runs. Members of the admin team can find this in our password manager. **Place it in `~/.kalkspace_ansible_vault_pass`.**

### Applying changes

Use the `site.yml` playbook to apply changes to a production node. You need to have your SSH key in `allowed_hosts` of the `root` user on the host.

```sh
ansible-playbook site.yml --diff
```
