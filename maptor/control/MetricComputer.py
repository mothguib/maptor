import numpy as np

from maptor import Metrics


class MetricComputer:
    def __init__(self):
        # Value of metrics at the time t
        self.metrics = np.array([0, 0, 0, 0, 0, 0], dtype=np.float)

        # Numpy array of intervals
        self.intvls = np.array([], dtype=np.int32)

    def compute_metrics(self, t: int, idlss: np.ndarray):
        """
        Compute the metrics iteratively

        :param t:
        :type t:
        :param idlss:
        :type idlss:
        :return:
        :rtype:
        """

        self.metrics[Metrics.AGI] = self.compute_agi(t, idlss)
        self.metrics[Metrics.MI] = self.compute_mi()
        self.metrics[Metrics.MSI] = self.compute_msi()
        self.metrics[Metrics.MAXI] = self.compute_max_i()
        self.metrics[Metrics.VARI] = self.compute_var_i()
        self.metrics[Metrics.SDI] = np.sqrt(self.metrics[Metrics.VARI])

    def get_intvls(self, t: int, idlss: np.ndarray):
        """
        Retrieve the intervals from the list of idlenesses

        :param t:
        :type t:
        :param idlss:
        :type idlss:
        :return:
        :rtype:
        """
        previidls = np.array(idlss[t - 1], dtype=np.int16)
        idls = np.array(idlss[t], dtype=np.int16)

        # Indices of idleness reinitialised at the time t
        ris = np.where(idls == 0)[0]

        self.intvls = np.append(self.intvls, previidls[ris] - idls[ris],
                                axis=0)

    def compute_agi(self, t: int, idlss: np.ndarray) -> float:
        """
        Compute the average graph idleness

        :param t:
        :type t:
        :param idlss:
        :type idlss:
        :return:
        :rtype:
        """
        return np.mean(np.mean(idlss))

    def compute_mi(self) -> float:
        """
        Compute the mean interval

        :return:
        :rtype:
        """
        return np.sum(self.intvls) / len(self.intvls)

    def compute_msi(self) -> float:
        """
        Compute the mean square interval

        :return:
        :rtype:
        """
        return np.sqrt(np.dot(self.intvls, self.intvls) / len(
            self.intvls))

    def compute_max_i(self) -> float:
        """
        Compute the maximum interval

        :return:
        :rtype:
        """
        return np.max(self.intvls)

    def compute_var_i(self) -> float:
        """
        Compute the variance of interval

        :return:
        :rtype:
        """
        mi = self.compute_mi()
        msi = self.compute_msi()

        return msi * msi - mi * mi
