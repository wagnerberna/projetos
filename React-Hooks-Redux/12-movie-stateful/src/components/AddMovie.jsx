import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddMovie extends Component {
  constructor() {
    super();
    this.state = {
      subtitle: '',
      title: '',
      imagePath: '',
      storyline: '',
      rating: 0,
      genre: 'action',
    };
    this.handleChange = this.handleChange.bind(this);
    this.sendButton = this.sendButton.bind(this);
    this.reset = this.reset.bind(this);
  }

  handleChange({ target }) {
    const { name, value } = target;
    this.setState({
      [name]: value,
    });
  }

  inputTitle(title) {
    return (
      <label data-testid="title-input-label" htmlFor="title-input">
        Título
        <input
          data-testid="title-input"
          name="title"
          type="text"
          value={ title }
          onChange={ this.handleChange }
        />
      </label>
    );
  }

  inputSubtitle(subtitle) {
    return (
      <label data-testid="subtitle-input-label" htmlFor="subtitle-input">
        Subtítulo
        <input
          data-testid="subtitle-input"
          name="subtitle"
          type="text"
          value={ subtitle }
          onChange={ this.handleChange }
        />
      </label>
    );
  }

  inputImagePath(imagePath) {
    return (
      <label data-testid="image-input-label" htmlFor="imagePath">
        Imagem
        <input
          data-testid="image-input"
          name="imagePath"
          type="text"
          value={ imagePath }
          onChange={ this.handleChange }
        />
      </label>
    );
  }

  inputStoryline(storyline) {
    return (
      <label data-testid="storyline-input-label" htmlFor="storyline-input">
        Sinopse
        <textarea
          data-testid="storyline-input"
          name="storyline"
          value={ storyline }
          onChange={ this.handleChange }
        />
      </label>
    );
  }

  inputRating(rating) {
    return (
      <label data-testid="rating-input-label" htmlFor="rating-input">
        Avaliação
        <input
          data-testid="rating-input"
          name="rating"
          type="number"
          value={ rating }
          onChange={ this.handleChange }
        />
      </label>
    );
  }

  inputGenre(genre) {
    return (
      <label data-testid="genre-input-label" htmlFor="genre-input">
        Gênero
        <select
          data-testid="genre-input"
          name="genre"
          value={ genre }
          onChange={ this.handleChange }
        >
          <option data-testid="genre-option" value="action">Ação</option>
          <option data-testid="genre-option" value="comedy">Comédia</option>
          <option data-testid="genre-option" value="thriller">Suspense</option>
        </select>
      </label>
    );
  }

  sendButton(reset) {
    return (
      <button
        data-testid="send-button"
        type="button"
        onClick={ reset }
      >
        Adicionar filme
      </button>
    );
  }

  reset() {
    // e.preventDefault();
    const { onClick } = this.props;
    onClick(this.state);
    this.setState({
      subtitle: '',
      title: '',
      imagePath: '',
      storyline: '',
      rating: 0,
      genre: 'action',
    });
  }

  render() {
    const { subtitle, title, imagePath, storyline,
      rating, genre } = this.state;
    return (
      <form data-testid="add-movie-form">
        {this.inputTitle(title)}
        {this.inputSubtitle(subtitle)}
        {this.inputImagePath(imagePath)}
        {this.inputStoryline(storyline)}
        {this.inputRating(rating)}
        {this.inputGenre(genre)}
        {this.sendButton(() => this.reset())}
      </form>
    );
  }
}

AddMovie.propTypes = {
  onClick: PropTypes.func.isRequired,
};

export default AddMovie;
