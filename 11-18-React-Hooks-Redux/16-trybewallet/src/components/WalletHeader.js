import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

class WalletHeader extends Component {
  expensesSum() {
    const { expensesStore } = this.props;
    // console.log(expensesStore[0]);
    const expensesMap = expensesStore.map((el) => {
      const { currency, value, exchangeRates } = el;
      // console.log(currency, value, exchangeRates);
      const exchangeRatesNumber = Number(exchangeRates[currency].ask);
      // console.log(exchangeRatesNumber);
      const valueNumber = Number(value);
      // console.log(valueNumber);
      const total = exchangeRatesNumber * valueNumber;
      // console.log(total);
      return total;
    });
    // console.log(expensesMap);
    return expensesMap.reduce((sum, expense) => sum + expense, 0);
  }

  render() {
    const { emailStore } = this.props;
    return (
      <header>
        <ul>
          <li data-testid="email-field">{`Usuário Logado: ${emailStore}`}</li>
          <li data-testid="total-field">
            Total: R$
            {this.expensesSum()}
          </li>
          <li data-testid="header-currency-field">Câmbio: BRL </li>
        </ul>
      </header>
    );
  }
}

WalletHeader.propTypes = {
  emailStore: PropTypes.string.isRequired,
  expensesStore: PropTypes.func.isRequired,
};

const mapStateToProps = (state) => ({
  emailStore: state.user.email,
  expensesStore: state.wallet.expenses,
});

export default connect(mapStateToProps, null)(WalletHeader);
