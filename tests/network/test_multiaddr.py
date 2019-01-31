from libp2p.network.multiaddr import MultiAddr

# This function is a tool for test function, this is why it not must by test_ to be ignored by pytest.
def verify_options(addr, options):
    addr_opts = addr.to_options()

    # Check if key are the same
    # Sort because we don't care about the key order, only keys itself are importent.
    # Join because if you compare list, python will compare pointer not content.
    addr_key = " ".join(sorted(addr_opts.keys()))
    opts_key = " ".join(sorted(options.keys()))
    assert addr_key == opts_key

    # Check if key content is as expected
    for k in options.keys():
        assert addr_opts[k] == options[k]

def test_simple_address():
    verify_options(MultiAddr("/ip4/192.168.0.76/udp/8000"), {"family": "ipv4", "host": "192.168.0.76", "transport": "udp", "port": "8000"})

def test_no_address():
    verify_options(MultiAddr(""), {"family": None, "host": None, "transport": None, "port": None})
