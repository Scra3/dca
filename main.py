#!/usr/bin/env python3

import constants
import dca_runner as runner
import model


def job():
    with open(constants.DCA_CONFIGURATION_FILE) as json_file:
        dca_configuration: model.DcaConfiguration = model.DcaConfiguration.serialise(
            json_file.read()
        )
    dca_runner = runner.DcaRunner(
        broker=model.Broker(), dca_configuration=dca_configuration
    )
    dca_runner.run()


if __name__ == "__main__":
    job()
